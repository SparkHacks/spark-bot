import discord
from discord.ext import commands

import logging

logger = logging.getLogger(__name__)

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.bot.user} is ready and online!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.guild.system_channel.send(f"Welcome to the SparkHacks 2026 Board, {member.mention}!")

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot)) 