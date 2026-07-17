import discord


# Mod commands
def MOD_BAN(member: discord.Member):
    return discord.Embed(
        description=f"{member.mention} has been banned.",
        color=discord.Color.red(),
    )


def MOD_UNBAN(user: discord.User):
    return discord.Embed(
        description=f"{user.mention} has been unbanned.",
        color=discord.Color.green(),
    )


def MOD_KICK(member: discord.Member):
    return discord.Embed(
        description=f"{member.mention} has been kicked.",
        color=discord.Color.red(),
    )


_DURATION_LABELS = {
    60: "60 seconds",
    300: "5 minutes",
    600: "10 minutes",
    3600: "1 hour",
    86400: "1 day",
    604800: "1 week",
}


def MOD_MUTE(member: discord.Member, duration: int):
    return discord.Embed(
        description=f"{member.mention} has been muted for {_DURATION_LABELS[duration]}.",
        color=discord.Color.red(),
    )


def MOD_UNMUTE(member: discord.Member):
    return discord.Embed(
        description=f"{member.mention} has been unmuted.",
        color=discord.Color.green(),
    )


# Role commands
def ROLE_ADD(member: discord.Member, role: discord.Role):
    return discord.Embed(
        description=f"Added {role.mention} role to {member.mention}",
        color=discord.Color.green(),
    )


def ROLE_REMOVE(member: discord.Member, role: discord.Role):
    return discord.Embed(
        description=f"Removed {role.mention} role from {member.mention}",
        color=discord.Color.red(),
    )


ROLE_FORBIDDEN = discord.Embed(
    description="The bot's role is not high enough to manage that role.",
    color=discord.Color.red(),
)

ROLE_HIERARCHY = discord.Embed(
    description="You cannot manage a role at or above your own highest role.",
    color=discord.Color.red(),
)
