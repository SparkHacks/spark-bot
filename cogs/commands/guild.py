import logging

import discord
from discord.ext import commands

from config import board, hackathon, permissions
from static import embeds
from utils.dataclasses import Channel, ChannelCategory
from utils.guilds import is_board_guild, is_hackathon_guild

logger = logging.getLogger(__name__)


async def setup_guild(ctx: discord.ApplicationContext):
    logger.info(f"{ctx.guild.name} server setup started by {ctx.author}")

    if is_board_guild(ctx.guild.name):
        roles = board.roles.ROLES
        channels = board.channels.CHANNELS

        welcome_channel = board.channels.WELCOME
        logs_channel = board.channels.LOGS
        rules_channel = None
    elif is_hackathon_guild(ctx.guild.name):
        roles = hackathon.roles.ROLES
        channels = hackathon.channels.CHANNELS

        welcome_channel = hackathon.channels.WELCOME
        logs_channel = hackathon.channels.SYS_LOGS
        rules_channel = hackathon.channels.RULES
    else:
        return

    for role in roles:
        await ctx.guild.create_role(
            name=role.name,
            permissions=role.permissions,
            color=role.color,
            hoist=role.hoist,
            mentionable=role.mentionable,
        )

    for item in channels:
        overwrites = {
            ctx.guild.default_role: permissions.overwrites.DENY,
            discord.utils.get(
                ctx.guild.roles, name="Board"
            ): permissions.overwrites.VIEW,
        }

        for role, overwrite in item.overwrites.items():
            overwrites[
                (
                    ctx.guild.default_role
                    if role.name == "@everyone"
                    else discord.utils.get(ctx.guild.roles, name=role.name)
                )
            ] = overwrite

        if isinstance(item, Channel):
            match item.type:
                case "text" | "announcement":
                    await ctx.guild.create_text_channel(
                        name=item.name, overwrites=overwrites
                    )
                case "voice":
                    await ctx.guild.create_voice_channel(
                        name=item.name, overwrites=overwrites
                    )
                case "forum":
                    await ctx.guild.create_forum_channel(
                        name=item.name, overwrites=overwrites
                    )

        elif isinstance(item, ChannelCategory):
            category_channel = await ctx.guild.create_category(
                name=item.name, overwrites=overwrites
            )

            for channel in item.channels:
                channel_overwrites = {**overwrites}

                for role, overwrite in channel.overwrites.items():
                    channel_overwrites[
                        (
                            ctx.guild.default_role
                            if role.name == "@everyone"
                            else discord.utils.get(
                                ctx.guild.roles, name=role.name
                            )
                        )
                    ] = overwrite

                match channel.type:
                    case "text" | "announcement":
                        await ctx.guild.create_text_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=channel_overwrites,
                        )
                    case "voice":
                        await ctx.guild.create_voice_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=channel_overwrites,
                        )
                    case "forum":
                        await ctx.guild.create_forum_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=channel_overwrites,
                        )

    await ctx.guild.default_role.edit(permissions=permissions.EVERYONE)
    await ctx.guild.edit(
        system_channel=discord.utils.get(
            ctx.guild.channels, name=welcome_channel.name
        ),
        system_channel_flags=discord.SystemChannelFlags(
            join_notifications=False,
            join_notification_replies=False,
            premium_subscriptions=False,
            guild_reminder_notifications=False,
        ),
        default_notifications=discord.NotificationLevel.only_mentions,
    )

    if rules_channel:
        await discord.utils.get(
            ctx.guild.channels, name=rules_channel.name
        ).send(embed=embeds.rules.RULES)

    await discord.utils.get(ctx.guild.channels, name=logs_channel.name).send(
        embed=embeds.commands.SETUP_SUCCESS
    )

    logger.info(f"{ctx.guild.name} server was set up by {ctx.author}")


async def wipe_guild(ctx: discord.ApplicationContext):
    logger.info(f"{ctx.guild.name} server wipe started by {ctx.author}")

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            logger.error(f"Error deleting channel {channel.name}: {e}")

    for role in ctx.guild.roles:
        if role.name == "@everyone" or ctx.guild.me.top_role <= role:
            continue
        try:
            await role.delete()
        except Exception as e:
            logger.error(f"Error deleting role {role.name}: {e}")

    logger.info(f"{ctx.guild.name} server was wiped by {ctx.author}")


class WipeView(discord.ui.View):
    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(timeout=30)
        self.ctx = ctx

    async def interaction_check(
        self, interaction: discord.Interaction
    ) -> bool:
        return interaction.user.id == self.ctx.author.id

    @discord.ui.button(label="Wipe & Setup", style=discord.ButtonStyle.danger)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.defer(ephemeral=True)
        try:
            await interaction.edit_original_response(view=None)
        except discord.NotFound:
            pass

        await wipe_guild(self.ctx)
        await setup_guild(self.ctx)

        self.stop()

    @discord.ui.button(label="Abort", style=discord.ButtonStyle.secondary)
    async def abort(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.edit_message(
            embed=embeds.commands.SETUP_ABORT, view=None
        )
        self.stop()

    async def on_timeout(self):
        try:
            await self.ctx.edit(embed=embeds.commands.SETUP_ABORT, view=None)
        except discord.NotFound:
            pass


class GuildCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    guild = discord.SlashCommandGroup(
        name="guild",
        description="Manage a guild",
        default_member_permissions=discord.Permissions(administrator=True),
    )

    @guild.command(name="setup", description="Set up a server")
    async def setup(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)

        # Show a view if there are not only @everyone and the bot's role
        # or is not only the channel where the command is called
        if len(ctx.guild.roles) > 2 or len(ctx.guild.channels) > 1:
            await ctx.edit(
                embed=embeds.commands.SETUP_CONFIRM, view=WipeView(ctx)
            )
            return

        await setup_guild(ctx)
        await ctx.edit(content="\u200b")

    @guild.command(name="wipe", description="Wipe a server")
    async def wipe(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)

        await wipe_guild(ctx)
        try:
            await ctx.edit(content="\u200b")
        except discord.NotFound:
            pass


def setup(bot: commands.Bot):
    bot.add_cog(GuildCommands(bot))
