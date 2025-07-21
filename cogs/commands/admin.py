import discord
from discord.ext import commands

import logging

from configs.board.channels import CHANNELS, CATEGORIES
from configs.board.roles import ROLES

logger = logging.getLogger(__name__)

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="setup_board")
    @commands.has_permissions(administrator=True)
    async def setup_board(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        for role in ROLES:
            await guild.create_role(name=role.name, permissions=role.permissions, color=role.color)

        for channel in CHANNELS:
            await guild.create_text_channel(name=channel.name)

        for category in CATEGORIES:
            category.channel = await guild.create_category(name=category.name)

            for channel in category.channels:
                match channel.type:
                    case "text":
                        await guild.create_text_channel(name=channel.name, category=category.channel)
                    case "voice":
                        await guild.create_voice_channel(name=channel.name, category=category.channel)
                    case _:
                        logger.error(f"Unknown channel type: {channel.type}.")

        await guild.edit(system_channel=discord.utils.get(guild.channels, name="📊logs📈"))
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