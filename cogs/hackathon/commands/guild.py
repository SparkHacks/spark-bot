import discord

import utils.commands.guild
from configs.hackathon.channels import (
    CHANNELS,
    RULES_CHANNEL_NAME,
    WELCOME_CHANNEL_NAME,
)
from configs.hackathon.roles import ROLES
from configs.permissions import DEFAULT
from configs.permissions.overwrites import READ_ONLY


async def setup(guild: discord.Guild):
    await utils.commands.guild.setup(guild, ROLES, CHANNELS)

    await guild.default_role.edit(permissions=DEFAULT)
    await discord.utils.get(
        guild.channels, name=WELCOME_CHANNEL_NAME
    ).set_permissions(guild.default_role, overwrite=READ_ONLY)
    await discord.utils.get(
        guild.channels, name=RULES_CHANNEL_NAME
    ).set_permissions(guild.default_role, overwrite=READ_ONLY)
