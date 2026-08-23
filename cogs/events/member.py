import logging

import discord
from discord.ext import commands

from static import embeds
from util.channels import get_logs_channel
from util.enums import LogsType
from util.events import get_audit_log_entry

logger = logging.getLogger(__name__)


class MemberEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        audit_log_entry = await get_audit_log_entry(
            guild, discord.AuditLogAction.ban, user.id
        )
        if audit_log_entry and audit_log_entry.user.bot:
            return

        moderator = audit_log_entry.user if audit_log_entry else guild.me
        reason = audit_log_entry.reason if audit_log_entry else None

        await get_logs_channel(guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_BANNED(user, moderator, reason)
        )
        logger.info(f"{user} was banned from {guild.name} server by {moderator}")

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        audit_log_entry = await get_audit_log_entry(
            guild, discord.AuditLogAction.unban, user.id
        )
        if audit_log_entry and audit_log_entry.user.bot:
            return

        moderator = audit_log_entry.user if audit_log_entry else guild.me
        reason = audit_log_entry.reason if audit_log_entry else None

        await get_logs_channel(guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_UNBANNED(user, moderator, reason)
        )
        logger.info(f"{user} was unbanned from {guild.name} server by {moderator}")

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if after.bot:
            return

        member_logs_channel = get_logs_channel(before.guild, LogsType.MEMBER)
        mod_logs_channel = get_logs_channel(before.guild, LogsType.MOD)

        if before.nick != after.nick:
            before_nick = before.nick or before.name
            after_nick = after.nick or after.name

            await member_logs_channel.send(
                embed=embeds.events.NICKNAME_CHANGED(after, before_nick, after_nick)
            )
            logger.info(
                f"{after} changed nickname from {before_nick} to {after_nick} in {before.guild.name} server"
            )

        if before.communication_disabled_until != after.communication_disabled_until:
            audit_log_entry = await get_audit_log_entry(
                before.guild, discord.AuditLogAction.member_update, after.id
            )
            if audit_log_entry and audit_log_entry.user.bot:
                pass
            else:
                moderator = audit_log_entry.user if audit_log_entry else before.guild.me
                reason = audit_log_entry.reason if audit_log_entry else None

                if after.communication_disabled_until:
                    await mod_logs_channel.send(
                        embed=embeds.events.MEMBER_MUTED(after, moderator, reason)
                    )
                    logger.info(
                        f"{after} was muted in {before.guild.name} server by {moderator}"
                    )
                else:
                    await mod_logs_channel.send(
                        embed=embeds.events.MEMBER_UNMUTED(after, moderator, reason)
                    )
                    logger.info(
                        f"{after} was unmuted in {before.guild.name} server by {moderator}"
                    )

        added = set(after.roles) - set(before.roles)
        removed = set(before.roles) - set(after.roles)

        for role in added:
            await member_logs_channel.send(embed=embeds.events.ROLE_GIVEN(after, role))
            logger.info(
                f"{role.name} role given to {after} in {before.guild.name} server"
            )
        for role in removed:
            await member_logs_channel.send(
                embed=embeds.events.ROLE_REMOVED(after, role)
            )
            logger.info(
                f"{role.name} role removed from {after} in {before.guild.name} server"
            )


def setup(bot: commands.Bot):
    bot.add_cog(MemberEvents(bot))
