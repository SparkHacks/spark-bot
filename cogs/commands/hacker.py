import discord
from discord.ext import commands

import logging

logger = logging.getLogger(__name__)

class Hacker(commands.Cog):
    def __init__(self, bot: commands.Bot): 
        self.bot = bot

    @commands.slash_command(description="Sends SparkHacks bot's latency") 
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Pong! Latency is {self.bot.latency}")
        logger.info(f"{ctx.author} used \"pong\" command.")

    @commands.slash_command(name="echo", description="Echo back your message")
    async def echo(self, ctx: discord.ApplicationContext, message: str):
        await ctx.respond(message)
        logger.info(f"{ctx.author} used \"echo\" command.")

def setup(bot: commands.Bot):
    bot.add_cog(Hacker(bot)) 