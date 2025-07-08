import discord
from discord.ext import commands

import logging

logger = logging.getLogger(__name__)

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync_commands(self, ctx: commands.Context):
        await self.bot.sync_commands()
        await ctx.send("Global commands synced successfully")
        logger.info(f"{ctx.author} synced commands globally.")

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot)) 