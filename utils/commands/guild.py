import discord

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
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False)
        }

        for role in [
            discord.utils.get(guild.roles, name=role.name)
            for role in channel.roles
        ]:
            overwrites[role] = discord.PermissionOverwrite(view_channel=True)

        if isinstance(channel, Channel):
            await guild.create_text_channel(
                name=channel.name, overwrites=overwrites
            )
        elif isinstance(channel, Category):
            category = channel

            category.channel = await guild.create_category(
                name=category.name, overwrites=overwrites
            )

            for channel in category.channels:
                match channel.type:
                    case "text":
                        await guild.create_text_channel(
                            name=channel.name, category=category.channel
                        )
                    case "voice":
                        await guild.create_voice_channel(
                            name=channel.name, category=category.channel
                        )
                    case "forum":
                        await guild.create_forum_channel(
                            name=channel.name, category=category.channel
                        )
