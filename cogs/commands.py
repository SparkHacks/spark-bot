import discord
from discord.ext import commands

import logging

from utils.dataclasses import Category, Channel, Role

logger = logging.getLogger(__name__)

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @classmethod
    async def setup( 
            cls,
            ctx: commands.Context,
            roles: list[Role],
            channels: list[Channel|Category]):
        guild: discord.Guild = ctx.guild
        me: discord.Member = ctx.me

        for role in roles:
            await guild.create_role(
                name=role.name, 
                permissions=role.permissions, 
                color=role.color, 
                hoist=role.hoist
            )

        await me.add_roles(discord.utils.get(guild.roles, name="Bots"))

        for channel in channels:
            permission_overwrites = { 
                guild.default_role: discord.PermissionOverwrite(view_channel=False) 
            }

            for role in [discord.utils.get(guild.roles, name=role.name) for role in channel.roles]:
                permission_overwrites[role] = discord.PermissionOverwrite(view_channel=True)

            if isinstance(channel, Channel):
                await guild.create_text_channel(name=channel.name, overwrites=permission_overwrites)
            elif isinstance(channel, Category):
                category = channel

                category.channel = await guild.create_category(name=category.name, overwrites=permission_overwrites)

                for channel in category.channels:
                    match channel.type:
                        case "text":
                            await guild.create_text_channel(name=channel.name, category=category.channel)
                        case "voice":
                            await guild.create_voice_channel(name=channel.name, category=category.channel)

        await ctx.channel.delete()

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