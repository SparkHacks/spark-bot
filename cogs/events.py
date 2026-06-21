import logging

import discord
from discord.ext import commands

from config import hackathon, roles
from static import embeds
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
            f"{', '.join([guild.name for guild in self.bot.guilds])}"
        )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if is_board_guild(member.guild.name):
            await member.add_roles(
                discord.utils.get(member.guild.roles, name=roles.BOARD.name)
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

            await discord.utils.get(
                member.guild.channels,
                name=hackathon.channels.GATEWAY_LOGS.name,
            ).send(embed=embeds.events.MEMBER_JOINED(member))

        await member.guild.system_channel.send(
            embed=embeds.events.WELCOME(member)
        )

        logger.info(f"{member} joined {member.guild.name}")

    @commands.Cog.listener()
    async def on_member_update(
        self, before: discord.Member, after: discord.Member
    ):
        if not is_hackathon_guild(before.guild.name):
            return

        added = set(after.roles) - set(before.roles)
        removed = set(before.roles) - set(after.roles)

        if not added and not removed:
            return

        logs_channel = discord.utils.get(
            before.guild.channels, name=hackathon.channels.MEMBER_LOGS.name
        )

        for role in added:
            await logs_channel.send(
                embed=embeds.events.ROLE_GIVEN(after, role)
            )
            logger.info(f"{role.name} given to {after} in {before.guild.name}")
        for role in removed:
            await logs_channel.send(
                embed=embeds.events.ROLE_REMOVED_(after, role)
            )
            logger.info(
                f"{role.name} removed from {after} in {before.guild.name}"
            )

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if not is_hackathon_guild(member.guild.name):
            return

        await discord.utils.get(
            member.guild.channels,
            name=hackathon.channels.GATEWAY_LOGS.name,
        ).send(embed=embeds.events.MEMBER_LEFT(member))

        logger.info(f"{member} left {member.guild.name}")


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
