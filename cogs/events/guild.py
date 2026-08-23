import logging

import discord
from discord.ext import commands

from config import board, hackathon, permissions, roles
from static import embeds
from util.dataclasses import ChannelCategory, ForumChannel, TextChannel, VoiceChannel
from util.enums import GuildType
from util.guilds import get_guild_type

logger = logging.getLogger(__name__)


class GuildEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if guild.channels:
            logger.info(f"{guild.name} server wipe started")

            for channel in guild.channels:
                try:
                    await channel.delete()
                except Exception as e:
                    logger.error(f"Error deleting channel {channel.name}: {e}")

            # Roles are not wiped since Discord blocks deleting roles above
            # the bot's managed role, which can't be repositioned via the API.
            # Assumes a fresh server with no prior roles but some channels

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

        for channel in channels:
            overwrites = {
                guild.default_role: permissions.overwrites.DENY,
                discord.utils.get(
                    guild.roles, name="Board"
                ): permissions.overwrites.VIEW,
            }
            for role, overwrite in channel.overwrites.items():
                overwrites[
                    (
                        guild.default_role
                        if role.name == "@everyone"
                        else discord.utils.get(guild.roles, name=role.name)
                    )
                ] = overwrite

            if isinstance(channel, ChannelCategory):
                category_channel = await guild.create_category(
                    name=channel.name, overwrites=overwrites
                )

                items = []

                for ch in channel.channels:
                    ch_overwrites = {**overwrites}
                    for role, overwrite in ch.overwrites.items():
                        ch_overwrites[
                            (
                                guild.default_role
                                if role.name == "@everyone"
                                else discord.utils.get(guild.roles, name=role.name)
                            )
                        ] = overwrite

                    items.append((ch, ch_overwrites, category_channel))
            else:
                items = [(channel, overwrites, None)]

            for ch, ch_overwrites, category in items:
                if isinstance(ch, TextChannel):
                    await guild.create_text_channel(
                        name=ch.name,
                        topic=ch.topic,
                        category=category,
                        overwrites=ch_overwrites,
                    )
                elif isinstance(ch, VoiceChannel):
                    await guild.create_voice_channel(
                        name=ch.name,
                        category=category,
                        overwrites=ch_overwrites,
                    )
                elif isinstance(ch, ForumChannel):
                    forum_channel = await guild.create_forum_channel(
                        name=ch.name,
                        topic=ch.post_guidelines,
                        category=category,
                        overwrites=ch_overwrites,
                    )
                    await forum_channel.edit(
                        available_tags=list(ch.tags),
                        default_reaction_emoji=ch.default_reaction,
                    )
                    if ch.require_tag:
                        await forum_channel.edit(require_tag=True)

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
            embed=embeds.events.SETUP_SUCCESS(guild)
        )

        await guild.me.add_roles(discord.utils.get(guild.roles, name=roles.BOTS.name))

        logger.info(f"{guild.name} server was set up")


def setup(bot: commands.Bot):
    bot.add_cog(GuildEvents(bot))
