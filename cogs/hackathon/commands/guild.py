import discord

import embeds
import utils.commands.guild
from configs.hackathon.channels import (
    CHANNELS,
    INTRODUCTIONS_CHANNEL_NAME,
    RULES_CHANNEL_NAME,
    WELCOME_CHANNEL_NAME,
)
from configs.hackathon.roles import ROLES
from configs.permissions import DEFAULT
from configs.permissions.overwrites import READ_ONLY, READ_WRITE


async def setup(guild: discord.Guild):
    await utils.commands.guild.setup(guild, ROLES, CHANNELS)

    await guild.default_role.edit(permissions=DEFAULT)

    welcome_channel = discord.utils.get(
        guild.channels, name=WELCOME_CHANNEL_NAME
    )
    rules_channel = discord.utils.get(guild.channels, name=RULES_CHANNEL_NAME)
    introductions_channel = discord.utils.get(
        guild.channels, name=INTRODUCTIONS_CHANNEL_NAME
    )

    await welcome_channel.set_permissions(
        guild.default_role, overwrite=READ_ONLY
    )
    await rules_channel.set_permissions(
        guild.default_role, overwrite=READ_ONLY
    )
    await introductions_channel.set_permissions(
        guild.default_role, overwrite=READ_WRITE
    )

    await guild.edit(system_channel=welcome_channel)

    await rules_channel.send(
        embed=embeds.rules,
        file=discord.File("assets/icon.png", filename="icon.png"),
    )
