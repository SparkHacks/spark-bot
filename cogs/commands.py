import discord
from discord.ext import commands

import logging

from configs.board.channels import WELCOME_CHANNEL_NAME
from utils.dataclasses import Category, Channel, Role, Team

logger = logging.getLogger(__name__)

class CommandHelpers:
    @classmethod
    async def setup(cls, ctx: commands.Context, roles: list[Role], channels: list[Channel|Category]):
        guild: discord.Guild = ctx.guild

        for role in roles:
            await guild.create_role(
                name=role.name, 
                permissions=role.permissions, 
                color=role.color, 
                hoist=role.hoist
            )

        me: discord.Member = ctx.me
        await me.add_roles(discord.utils.get(guild.roles, name="Bots"))

        for channel in channels:
            overwrites = { 
                guild.default_role: discord.PermissionOverwrite(view_channel=False) 
            }

            for role in [discord.utils.get(guild.roles, name=role.name) for role in channel.roles]:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

            if isinstance(channel, Channel):
                await guild.create_text_channel(name=channel.name, overwrites=overwrites)
            elif isinstance(channel, Category):
                category = channel

                category.channel = await guild.create_category(name=category.name, overwrites=overwrites)

                for channel in category.channels:
                    match channel.type:
                        case "text":
                            await guild.create_text_channel(name=channel.name, category=category.channel)
                        case "voice":
                            await guild.create_voice_channel(name=channel.name, category=category.channel)

        welcome_channel = discord.utils.get(guild.channels, name=WELCOME_CHANNEL_NAME)

        overwrite = welcome_channel.overwrites_for(guild.default_role)
        overwrite.view_channel = True

        await guild.edit(system_channel=welcome_channel)
        await welcome_channel.set_permissions(guild.default_role, overwrite=overwrite)

        await ctx.channel.delete()

    @classmethod
    async def sync_user(cls, member: discord.Member, teams: list[Team]):
        for team in teams:
            if member.id not in team.members:
                continue

            if team_role := discord.utils.get(member.guild.roles, name=team.name) and team_role not in member.roles:
                await member.add_roles(team_role)

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="wipe")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def wipe(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        for channel in guild.channels:
            try:
                await channel.delete()
            except Exception as e:
                logger.error(f"Error deleting channel {channel.name}: {e}")

        for role in guild.roles:
            if role.name == "@everyone" or guild.me.top_role <= role:
                continue
            
            try:
                await role.delete()
            except Exception as e:
                logger.error(f"Error deleting role {role.name}: {e}")

def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot)) 