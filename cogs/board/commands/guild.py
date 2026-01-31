import discord

import utils.commands.guild
from configs.board.channels import CHANNELS, WELCOME_CHANNEL_NAME
from configs.board.roles import ROLES


async def setup(guild: discord.Guild):
    await utils.commands.guild.setup(guild, ROLES, CHANNELS)

    welcome_channel = discord.utils.get(
        guild.channels, name=WELCOME_CHANNEL_NAME
    )

    overwrite = welcome_channel.overwrites_for(guild.default_role)
    overwrite.view_channel = True

    await welcome_channel.set_permissions(
        guild.default_role, overwrite=overwrite
    )

    await guild.edit(system_channel=welcome_channel)
