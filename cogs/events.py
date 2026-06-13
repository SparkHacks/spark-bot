import logging

import discord
from discord.ext import commands

import cogs.board.events
import cogs.hackathon.events
from utils.guilds import is_board_guild, is_hackathon_guild

logger = logging.getLogger(__name__)


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.bot.user.name} is ready and online!")
        logger.info(
            f"{self.bot.user.name} is connected to guilds: "
            f"{[f'{guild.name}' for guild in self.bot.guilds]}"
        )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        name = member.guild.name

        if is_board_guild(name):
            await cogs.board.events.on_member_join(member)
        elif is_hackathon_guild(name):
            await cogs.hackathon.events.on_member_join(member)


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
