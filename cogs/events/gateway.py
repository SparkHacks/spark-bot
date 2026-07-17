import logging

import discord
from discord.ext import commands

from config import hackathon, roles
from static import embeds
from utils.channels import get_logs_channel
from utils.enums import GuildType, LogsType
from utils.events import get_audit_log_entry
from utils.guilds import get_guild_type

logger = logging.getLogger(__name__)


class GatewayEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not member.bot:
            if get_guild_type(member.guild.name) == GuildType.BOARD:
                await member.add_roles(
                    discord.utils.get(member.guild.roles, name=roles.BOARD.name)
                )
            else:
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

            await member.guild.system_channel.send(
                embed=embeds.events.WELCOME(member),
                allowed_mentions=discord.AllowedMentions(users=True),
            )

        await get_logs_channel(member.guild, LogsType.GATEWAY).send(
            embed=embeds.events.MEMBER_JOINED(member)
        )
        logger.info(f"{member} joined {member.guild.name} server")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if member.id == self.bot.user.id:
            return

        kick_entry = await get_audit_log_entry(
            member.guild, discord.AuditLogAction.kick, member.id
        )
        ban_entry = await get_audit_log_entry(
            member.guild, discord.AuditLogAction.ban, member.id
        )

        if kick_entry and not kick_entry.user.bot:
            await get_logs_channel(member.guild, LogsType.MOD).send(
                embed=embeds.events.MEMBER_KICKED(
                    member, kick_entry.user, kick_entry.reason
                )
            )
            logger.info(
                f"{member} was kicked from {member.guild.name} server by {kick_entry.user}"
            )
        elif not kick_entry and not ban_entry:
            await get_logs_channel(member.guild, LogsType.GATEWAY).send(
                embed=embeds.events.MEMBER_LEFT(member)
            )
            logger.info(f"{member} left {member.guild.name} server")


def setup(bot: commands.Bot):
    bot.add_cog(GatewayEvents(bot))
