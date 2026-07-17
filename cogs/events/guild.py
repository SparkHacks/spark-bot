import logging

import discord
from discord.ext import commands

from config import board, hackathon, permissions, roles
from static import embeds
from utils.dataclasses import Channel, ChannelCategory
from utils.enums import GuildType
from utils.guilds import get_guild_type

logger = logging.getLogger(__name__)


class GuildEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        logger.info(f"{guild.name} server wipe started")

        for channel in guild.channels:
            try:
                await channel.delete()
            except Exception as e:
                logger.error(f"Error deleting channel {channel.name}: {e}")

        for role in guild.roles:
            if role.name == "@everyone" or guild.me.top_role <= role:
                continue
            try:
                await role.delete()
            except Exception as e:
                logger.error(f"Error deleting role {role.name}: {e}")

        logger.info(f"{guild.name} server was wiped")
        logger.info(f"{guild.name} server setup started")

        if get_guild_type(guild.name) == GuildType.BOARD:
            guild_roles = board.roles.ROLES
            channels = board.channels.CHANNELS
            welcome_channel = board.channels.WELCOME
            logs_channel = board.channels.LOGS
            rules_channel = None
        else:
            guild_roles = hackathon.roles.ROLES
            channels = hackathon.channels.CHANNELS
            welcome_channel = hackathon.channels.WELCOME
            logs_channel = hackathon.channels.SYS_LOGS
            rules_channel = hackathon.channels.RULES

        for role in guild_roles:
            await guild.create_role(
                name=role.name,
                permissions=role.permissions,
                color=role.color,
                hoist=role.hoist,
                mentionable=role.mentionable,
            )

        for item in channels:
            overwrites = {
                guild.default_role: permissions.overwrites.DENY,
                discord.utils.get(
                    guild.roles, name="Board"
                ): permissions.overwrites.VIEW,
            }

            for role, overwrite in item.overwrites.items():
                overwrites[
                    (
                        guild.default_role
                        if role.name == "@everyone"
                        else discord.utils.get(guild.roles, name=role.name)
                    )
                ] = overwrite

            if isinstance(item, Channel):
                match item.type:
                    case "text" | "announcement":
                        await guild.create_text_channel(
                            name=item.name, overwrites=overwrites
                        )
                    case "voice":
                        await guild.create_voice_channel(
                            name=item.name, overwrites=overwrites
                        )
                    case "forum":
                        await guild.create_forum_channel(
                            name=item.name, overwrites=overwrites
                        )

            elif isinstance(item, ChannelCategory):
                category_channel = await guild.create_category(
                    name=item.name, overwrites=overwrites
                )

                for channel in item.channels:
                    channel_overwrites = {**overwrites}

                    for role, overwrite in channel.overwrites.items():
                        channel_overwrites[
                            (
                                guild.default_role
                                if role.name == "@everyone"
                                else discord.utils.get(guild.roles, name=role.name)
                            )
                        ] = overwrite

                    match channel.type:
                        case "text" | "announcement":
                            await guild.create_text_channel(
                                name=channel.name,
                                category=category_channel,
                                overwrites=channel_overwrites,
                            )
                        case "voice":
                            await guild.create_voice_channel(
                                name=channel.name,
                                category=category_channel,
                                overwrites=channel_overwrites,
                            )
                        case "forum":
                            await guild.create_forum_channel(
                                name=channel.name,
                                category=category_channel,
                                overwrites=channel_overwrites,
                            )

        await guild.default_role.edit(permissions=permissions.EVERYONE)
        await guild.edit(
            system_channel=discord.utils.get(guild.channels, name=welcome_channel.name),
            system_channel_flags=discord.SystemChannelFlags(
                join_notifications=False,
                join_notification_replies=False,
                premium_subscriptions=False,
                guild_reminder_notifications=False,
            ),
            default_notifications=discord.NotificationLevel.only_mentions,
        )

        if rules_channel:
            rules_msg = await discord.utils.get(
                guild.channels, name=rules_channel.name
            ).send(embed=embeds.rules.RULES)
            await rules_msg.add_reaction("✅")

        await discord.utils.get(guild.channels, name=logs_channel.name).send(
            embed=embeds.commands.SETUP_SUCCESS
        )

        await guild.me.add_roles(discord.utils.get(guild.roles, name=roles.BOTS.name))

        logger.info(f"{guild.name} server was set up")


def setup(bot: commands.Bot):
    bot.add_cog(GuildEvents(bot))
