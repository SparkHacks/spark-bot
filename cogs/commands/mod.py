import logging
from datetime import timedelta

import discord
from discord.ext import commands

from static import embeds
from utils.channels import get_logs_channel
from utils.enums import LogsType

logger = logging.getLogger(__name__)


class ModCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.slash_command(name="ban", description="Ban a member")
    @discord.default_permissions(ban_members=True)
    @discord.option("member", description="Member to ban")
    @discord.option("reason", description="Reason for the ban")
    @discord.option(
        "preserve_messages", description="Whether to preserve member messages or not"
    )
    async def ban(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        reason: str = None,
        preserve_messages: bool = True,
    ):
        await ctx.defer(ephemeral=True)

        if ctx.guild.me.top_role <= member.top_role:
            await ctx.edit(embed=embeds.commands.ROLE_FORBIDDEN)
            return

        await member.ban(
            reason=reason, delete_message_seconds=0 if preserve_messages else 604800
        )

        await get_logs_channel(ctx.guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_BANNED(member, ctx.author, reason)
        )
        await ctx.edit(embed=embeds.commands.MOD_BAN(member))
        logger.info(f"{member} was banned from {ctx.guild.name} server by {ctx.author}")

    @discord.slash_command(name="unban", description="Unban a member")
    @discord.default_permissions(ban_members=True)
    @discord.option("user_id", description="User ID to unban")
    @discord.option("reason", description="Reason for the unban")
    async def unban(
        self,
        ctx: discord.ApplicationContext,
        user_id: str,
        reason: str = None,
    ):
        await ctx.defer(ephemeral=True)

        try:
            user = await ctx.bot.fetch_user(int(user_id))
        except (ValueError, discord.NotFound):
            await ctx.edit(
                embed=discord.Embed(
                    description="User not found. Make sure you're passing a valid user ID.",
                    color=discord.Color.red(),
                )
            )
            return

        await ctx.guild.unban(user, reason=reason)

        await get_logs_channel(ctx.guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_UNBANNED(user, ctx.author, reason)
        )
        await ctx.edit(embed=embeds.commands.MOD_UNBAN(user))
        logger.info(f"{user} was unbanned from {ctx.guild.name} server by {ctx.author}")

    @discord.slash_command(name="kick", description="Kick a member")
    @discord.default_permissions(kick_members=True)
    @discord.option("member", description="Member to kick")
    @discord.option("reason", description="Reason for the kick")
    async def kick(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        reason: str = None,
    ):
        await ctx.defer(ephemeral=True)

        if ctx.guild.me.top_role <= member.top_role:
            await ctx.edit(embed=embeds.commands.ROLE_FORBIDDEN)
            return

        await member.kick(reason=reason)

        await get_logs_channel(ctx.guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_KICKED(member, ctx.author, reason)
        )
        await ctx.edit(embed=embeds.commands.MOD_KICK(member))
        logger.info(f"{member} was kicked from {ctx.guild.name} server by {ctx.author}")

    @discord.slash_command(name="mute", description="Mute a member")
    @discord.default_permissions(moderate_members=True)
    @discord.option("member", description="Member to mute")
    @discord.option(
        "duration",
        int,
        description="Duration of the timeout",
        choices=[
            discord.OptionChoice("60 seconds", 60),
            discord.OptionChoice("5 minutes", 300),
            discord.OptionChoice("10 minutes", 600),
            discord.OptionChoice("1 hour", 3600),
            discord.OptionChoice("1 day", 86400),
            discord.OptionChoice("1 week", 604800),
        ],
    )
    @discord.option("reason", description="Reason for the mute")
    async def mute(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        duration: int,
        reason: str = None,
    ):
        await ctx.defer(ephemeral=True)

        if ctx.guild.me.top_role <= member.top_role:
            await ctx.edit(embed=embeds.commands.ROLE_FORBIDDEN)
            return

        await member.timeout(
            discord.utils.utcnow() + timedelta(seconds=duration), reason=reason
        )

        await get_logs_channel(ctx.guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_MUTED(member, ctx.author, reason)
        )
        await ctx.edit(embed=embeds.commands.MOD_MUTE(member, duration))
        logger.info(
            f"{member} was muted in {ctx.guild.name} server by {ctx.author} for {duration}s"
        )

    @discord.slash_command(name="unmute", description="Unmute a member")
    @discord.default_permissions(moderate_members=True)
    @discord.option("member", description="Member to unmute")
    @discord.option("reason", description="Reason for the unmute")
    async def unmute(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        reason: str = None,
    ):
        await ctx.defer(ephemeral=True)

        await member.remove_timeout(reason=reason)

        await get_logs_channel(ctx.guild, LogsType.MOD).send(
            embed=embeds.events.MEMBER_UNMUTED(member, ctx.author, reason)
        )
        await ctx.edit(embed=embeds.commands.MOD_UNMUTE(member))
        logger.info(f"{member} was unmuted in {ctx.guild.name} server by {ctx.author}")


def setup(bot: commands.Bot):
    bot.add_cog(ModCommands(bot))
