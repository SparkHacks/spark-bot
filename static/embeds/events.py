import discord

from static import colors


def WELCOME(member: discord.Member):
    return discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=f"Glad to see you here, {member.mention}!",
        color=colors.BOT,
    )


def ROLE_GIVEN(member: discord.Member, role: discord.Role):
    return (
        discord.Embed(
            description=f"{member.mention} was given the {role.mention} role",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow(),
        )
        .set_author(
            name=member.display_name, icon_url=member.display_avatar.url
        )
        .set_footer(text=f"ID: {member.id}")
    )


def ROLE_REMOVED_(member: discord.Member, role: discord.Role):
    return (
        discord.Embed(
            description=f"{member.mention} was removed from the {role.mention} role",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )
        .set_author(
            name=member.display_name, icon_url=member.display_avatar.url
        )
        .set_footer(text=f"ID: {member.id}")
    )
