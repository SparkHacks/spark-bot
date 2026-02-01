import discord

import utils.commands.role
from configs.hackathon.channels import WELCOME_CHANNEL_NAME
from configs.hackathon.roles import (
    EXPERIENCE_ROLE_CATEGORY,
    PERSONAL_ROLE_CATEGORY,
    TEAM_STATUS_ROLE_CATEGORY,
)


async def on_member_join(member: discord.Member):
    await utils.commands.role.sync(member.guild, [member])

    await member.add_roles(
        discord.utils.get(
            member.guild.roles, name=PERSONAL_ROLE_CATEGORY.name
        ),
        discord.utils.get(
            member.guild.roles, name=EXPERIENCE_ROLE_CATEGORY.name
        ),
        discord.utils.get(
            member.guild.roles, name=TEAM_STATUS_ROLE_CATEGORY.name
        ),
    )

    embed = discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=(f"Glad to see you here, {member.mention}!"),
        color=discord.Color(int("#A5A8C3"[1:], 16)),
    )

    await discord.utils.get(
        member.guild.channels, name=WELCOME_CHANNEL_NAME
    ).send(embed=embed)
