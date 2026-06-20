import logging

import discord
from discord.ext import commands

from config import hackathon
from static import embeds
from utils.guilds import is_board_guild, is_hackathon_guild

logger = logging.getLogger(__name__)


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if is_board_guild(member.guild.name):
            await member.add_roles(
                discord.utils.get(member.guild.roles, name="Board")
            )
        elif is_hackathon_guild(member.guild.name):
            await member.add_roles(
                discord.utils.get(
                    member.guild.roles,
                    name=hackathon.roles.categories.PERSONAL.name,
                ),
                discord.utils.get(
                    member.guild.roles,
                    name=hackathon.roles.categories.EXPERIENCE.name,
                ),
                discord.utils.get(
                    member.guild.roles,
                    name=hackathon.roles.categories.TEAM_STATUS.name,
                ),
            )

        await member.guild.system_channel.send(embed=embeds.WELCOME(member))
        logger.info(f"{member} joined {member.guild.name}")

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.bot.user.name} is ready and online!")
        logger.info(
            f"{self.bot.user.name} is connected to guilds: "
            f"{', '.join([guild.name for guild in self.bot.guilds])}"
        )


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
