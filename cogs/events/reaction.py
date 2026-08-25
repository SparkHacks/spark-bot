import logging

import discord
from discord.ext import commands

from config import hackathon
from util.enums import GuildType
from util.guilds import get_guild_type

logger = logging.getLogger(__name__)


class ReactionEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        if str(payload.emoji) != "✅":
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild or get_guild_type(guild.name) != GuildType.HACKATHON:
            return

        channel = guild.get_channel(payload.channel_id)
        if not channel or channel.name != hackathon.channels.RULES.name:
            return

        member = payload.member or guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        if {role.name for role in member.roles} & {
            hackathon.roles.BOARD.name,
            hackathon.roles.SPONSOR.name,
            hackathon.roles.JUDGE.name,
            hackathon.roles.MENTOR.name,
        }:
            return

        hacker_role = discord.utils.get(guild.roles, name=hackathon.roles.HACKER.name)
        if not hacker_role:
            return

        await member.add_roles(hacker_role)
        logger.info(
            f"{member} accepted rules and received Hacker role in {guild.name} server"
        )

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        if str(payload.emoji) != "✅":
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild or get_guild_type(guild.name) != GuildType.HACKATHON:
            return

        channel = guild.get_channel(payload.channel_id)
        if not channel or channel.name != hackathon.channels.RULES.name:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        hacker_role = discord.utils.get(guild.roles, name=hackathon.roles.HACKER.name)
        if not hacker_role or hacker_role not in member.roles:
            return

        await member.remove_roles(hacker_role)
        logger.info(
            f"{member} revoked rules acceptance and lost Hacker role in {guild.name} server"
        )


def setup(bot: commands.Bot):
    bot.add_cog(ReactionEvents(bot))
