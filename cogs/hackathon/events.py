import discord

import utils.commands.role
from configs.board.channels import WELCOME_CHANNEL_NAME


async def on_member_join(member: discord.Member):
    await utils.commands.role.sync(member.guild, member)

    welcome_channel = discord.utils.get(
        member.guild.channels, name=WELCOME_CHANNEL_NAME
    )

    embed = discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=(f"Glad to see you here, {member.mention}!"),
        color=discord.Color(int("#A5A8C3"[1:], 16)),
    )

    await welcome_channel.send(embed=embed)
