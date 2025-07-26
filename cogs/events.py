import discord
from discord.ext import commands

import logging

from configs.board.teams import TEAMS

logger = logging.getLogger(__name__)

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.bot.user.name} is ready and online!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):  
        for team in TEAMS:
            if member.name in team.members:
                await member.add_roles(discord.utils.get(member.guild.roles, name=team.name))
        
        await member.add_roles(discord.utils.get(member.guild.roles, name="Board"))

        await member.guild.system_channel.send(f"Welcome to the SparkHacks 2026 Board, {member.mention}!")

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot)) 