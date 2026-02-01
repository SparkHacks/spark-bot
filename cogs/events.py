import logging

import discord
from discord.ext import commands

import cogs.board.events
import cogs.hackathon.events
from configs.guilds import BOARD_GUILD_IDS, HACKATHON_GUILD_IDS

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
        guild_id = member.guild.id

        if guild_id in BOARD_GUILD_IDS:
            await cogs.board.events.on_member_join(member)
        elif guild_id in HACKATHON_GUILD_IDS:
            await cogs.hackathon.events.on_member_join(member)


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
