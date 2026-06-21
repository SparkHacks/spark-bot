import discord

SETUP_CONFIRM = discord.Embed(
    description="Server already has roles or channels. Wipe everything and set up from scratch?",
    color=discord.Color.orange(),
)

SETUP_ABORT = discord.Embed(
    description="Server setup was aborted.",
    color=discord.Color.dark_gray(),
)

SETUP_SUCCESS = discord.Embed(
    description="Server has been set up successfully!",
    color=discord.Color.green(),
)


def ROLE_ADD(member: discord.Member, role: discord.Role):
    return discord.Embed(
        description=f"Added {role.mention} to {member.mention}",
        color=discord.Color.green(),
    )


def ROLE_REMOVE(member: discord.Member, role: discord.Role):
    return discord.Embed(
        description=f"Removed {role.mention} from {member.mention}",
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
