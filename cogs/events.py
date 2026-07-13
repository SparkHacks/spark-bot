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
        logger.info(f"{member} joined {member.guild.name}")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
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
                f"{member} was kicked from {member.guild.name} by {kick_entry.user}"
            )
        elif not kick_entry and not ban_entry:
            await get_logs_channel(member.guild, LogsType.GATEWAY).send(
                embed=embeds.events.MEMBER_LEFT(member)
            )
            logger.info(f"{member} left {member.guild.name}")

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
        logger.info(f"{user} was banned from {guild.name} by {moderator}")

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
        logger.info(f"{user} was unbanned from {guild.name} by {moderator}")

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        member_logs_channel = get_logs_channel(before.guild, LogsType.MEMBER)
        mod_logs_channel = get_logs_channel(before.guild, LogsType.MOD)

        if before.nick != after.nick:
            before_nick = before.nick or before.name
            after_nick = after.nick or after.name

            await member_logs_channel.send(
                embed=embeds.events.NICKNAME_CHANGED(after, before_nick, after_nick)
            )
            logger.info(
                f"{after} changed nickname from {before_nick} to {after_nick} in {before.guild.name}"
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
                        f"{after} was muted in {before.guild.name} by {moderator}"
                    )
                else:
                    await mod_logs_channel.send(
                        embed=embeds.events.MEMBER_UNMUTED(after, moderator, reason)
                    )
                    logger.info(
                        f"{after} was unmuted in {before.guild.name} by {moderator}"
                    )

        added = set(after.roles) - set(before.roles)
        removed = set(before.roles) - set(after.roles)

        for role in added:
            await member_logs_channel.send(embed=embeds.events.ROLE_GIVEN(after, role))
            logger.info(f"Role {role.name} given to {after} in {before.guild.name}")
        for role in removed:
            await member_logs_channel.send(
                embed=embeds.events.ROLE_REMOVED(after, role)
            )
            logger.info(f"Role {role.name} removed from {after} in {before.guild.name}")

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return

        await get_logs_channel(message.guild, LogsType.MESSAGE).send(
            embed=embeds.events.MESSAGE_DELETED(message)
        )
        logger.info(
            f"Message by {message.author} deleted in {message.channel} channel in {message.guild.name}"
        )

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if after.author.bot or not after.guild or before.content == after.content:
            return

        await get_logs_channel(after.guild, LogsType.MESSAGE).send(
            embed=embeds.events.MESSAGE_EDITED(before, after)
        )
        logger.info(
            f"Message by {after.author} edited in {after.channel} channel in {after.guild.name}"
        )


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
