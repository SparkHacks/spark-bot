import discord

from configs.hackathon.roles import BOARD
from configs.permissions.overwrites import DENY, READ_WRITE
from utils.dataclasses import Category, Channel, Role


async def setup(
    guild: discord.Guild,
    roles: list[Role],
    channels: list[Channel | Category],
):
    for role in roles:
        await guild.create_role(
            name=role.name,
            permissions=role.permissions,
            color=role.color,
            hoist=role.hoist,
        )

    for channel in channels:
        overwrites = {}

        overwrites = {
            guild.default_role: DENY,
            discord.utils.get(guild.roles, name=BOARD.name): READ_WRITE,
        }

        for role, overwrite in channel.overwrites.items():
            overwrites[discord.utils.get(guild.roles, name=role.name)] = (
                overwrite
            )

        if isinstance(channel, Channel):
            await guild.create_text_channel(
                name=channel.name, overwrites=overwrites
            )
        elif isinstance(channel, Category):
            category = channel

            category_channel = await guild.create_category(
                name=category.name, overwrites=overwrites
            )

            for channel in category.channels:
                for role, overwrite in channel.overwrites.items():
                    overwrites[
                        discord.utils.get(guild.roles, name=role.name)
                    ] = overwrite

                match channel.type:
                    case "text":
                        await guild.create_text_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=overwrites,
                        )
                    case "voice":
                        await guild.create_voice_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=overwrites,
                        )
                    case "forum":
                        await guild.create_forum_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=overwrites,
                        )
