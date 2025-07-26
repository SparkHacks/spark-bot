import discord
from discord.ext import commands

import logging

from configs.board.channels import CHANNELS
from configs.board.roles import ROLES
from utils.dataclasses import Category, Channel

logger = logging.getLogger(__name__)

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="setup_board")
    @commands.has_permissions(administrator=True)
    async def setup_board(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        for role in ROLES:
            await guild.create_role(
                name=role.name, 
                permissions=role.permissions, 
                color=role.color, 
                hoist=role.hoist
            )

        channels = [item for item in CHANNELS if isinstance(item, Channel)]
        categories = [item for item in CHANNELS if isinstance(item, Category)]

        for channel in channels:
            await guild.create_text_channel(name=channel.name)

        await guild.edit(system_channel=discord.utils.get(guild.channels, name="🎉welcome👋"))

        for category in categories:
            overwrites = { 
                guild.default_role: discord.PermissionOverwrite(view_channel=False) 
            }

            for role in [discord.utils.get(guild.roles, name=role.name) for role in category.roles]:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

            category.channel = await guild.create_category(name=category.name, overwrites=overwrites)

            for channel in category.channels:
                match channel.type:
                    case "text":
                        await guild.create_text_channel(name=channel.name, category=category.channel)
                    case "voice":
                        await guild.create_voice_channel(name=channel.name, category=category.channel)

        await ctx.channel.delete()

    @commands.command(name="wipe")
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
    bot.add_cog(Admin(bot)) 