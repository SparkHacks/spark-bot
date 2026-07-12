import random

import discord

from static import colors

WELCOME_TEXTS = [
    "{mention} just landed",
    "{mention} just showed up",
    "{mention} joined the party",
    "{mention} is here",
    "Good to see you, {mention}",
    "Glad you're here, {mention}",
    "Yay you made it, {mention}",
]


def WELCOME(member: discord.Member):
    introduction_channel = discord.utils.find(
        lambda channel: "introductions" in channel.name, member.guild.channels
    )

    return discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=(
            f"{random.choice(WELCOME_TEXTS).format(mention=member.mention)}! "
            f"Head over to {introduction_channel.mention} and say hi!"
        ),
        color=colors.BOT,
    )


def MEMBER_JOINED(member: discord.Member):
    return (
        discord.Embed(
            description=f"{member.mention} {member.name}",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow(),
        )
        .set_author(name="Member Joined", icon_url=member.display_avatar.url)
        .set_thumbnail(url=member.display_avatar.url)
        .add_field(
            name="Account Created",
            value=discord.utils.format_dt(member.created_at, style="R"),
        )
        .set_footer(text=f"ID: {member.id}")
    )


def MEMBER_LEFT(member: discord.Member):
    return (
        discord.Embed(
            description=f"{member.mention} {member.name}",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )
        .set_author(name="Member Left", icon_url=member.display_avatar.url)
        .set_thumbnail(url=member.display_avatar.url)
        .set_footer(text=f"ID: {member.id}")
    )


def NICKNAME_CHANGED(
    member: discord.Member, before_nick: str, after_nick: str
):
    return (
        discord.Embed(
            description=f"{member.mention} nickname changed",
            color=colors.BOT,
            timestamp=discord.utils.utcnow(),
        )
        .set_author(name=member.name, icon_url=member.display_avatar.url)
        .add_field(name="Before", value=before_nick)
        .add_field(name="After", value=after_nick)
        .set_footer(text=f"ID: {member.id}")
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


def ROLE_REMOVED(member: discord.Member, role: discord.Role):
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


def MESSAGE_DELETED(message: discord.Message):
    return (
        discord.Embed(
            description=(
                f"Message sent by {message.author.mention} deleted in {message.channel.mention}\n"
                f"{message.content or '*No text content*'}"
            ),
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )
        .set_author(
            name=message.author.name,
            icon_url=message.author.display_avatar.url,
        )
        .set_footer(
            text=f"User ID: {message.author.id} • Message ID: {message.id}"
        )
    )


def MESSAGE_EDITED(before: discord.Message, after: discord.Message):
    return (
        discord.Embed(
            description=f"Message edited in {after.channel.mention} [Jump to Message]({after.jump_url})",
            color=colors.BOT,
            timestamp=discord.utils.utcnow(),
        )
        .set_author(
            name=after.author.name, icon_url=after.author.display_avatar.url
        )
        .add_field(name="Before", value=before.content or "*No text content*")
        .add_field(name="After", value=after.content or "*No text content*")
        .set_footer(text=f"User ID: {after.author.id}")
    )
