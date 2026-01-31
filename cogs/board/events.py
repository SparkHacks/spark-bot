import discord

from configs.board.channels import (
    INTRODUCTIONS_CHANNEL_NAME,
    WELCOME_CHANNEL_NAME,
)


async def on_member_join(member: discord.Member):
    await member.add_roles(discord.utils.get(member.guild.roles, name="Board"))

    welcome_channel = discord.utils.get(
        member.guild.channels, name=WELCOME_CHANNEL_NAME
    )
    introductions_channel = discord.utils.get(
        member.guild.channels, name=INTRODUCTIONS_CHANNEL_NAME
    )

    embed = discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=(
            f"Glad to see you here, {member.mention}! "
            f"Make sure to check out {introductions_channel.mention} "
            "and introduce yourself to everyone!"
        ),
        color=discord.Color(int("#A5A8C3"[1:], 16)),
    )

    if len(member.roles) == 1:
        embed.set_footer(
            f"{member.guild.owner.mention}, "
            f"please assign appropriate roles to {member.display_name}!"
        )

    await welcome_channel.send(embed=embed)
