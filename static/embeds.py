import discord

from static import colors

# Special
RULES = (
    discord.Embed(
        description="Welcome! Please read and follow these rules to keep the hackathon inclusive, productive, and fun for everyone.\n",
        color=colors.BOT,
    )
    .set_author(name="SparkHacks Rules")
    .add_field(
        name="🧠 Rule 1 — Be Respectful 🤝",
        value=(
            "Be kind and treat everyone with respect.\n"
            "**Zero tolerance for:** harassment, discrimination, hate speech, racism, sexism, homophobia, transphobia, ableism, slurs, impersonation, or sharing personal information without consent."
        ),
        inline=False,
    )
    .add_field(
        name="🚫 Rule 2 — No NSFW/NSFL Content 🔞",
        value=(
            "NSFW or NSFL content is **not allowed**.\n"
            "**Includes:** messages, images, links, usernames, nicknames, and profile pictures."
        ),
        inline=False,
    )
    .add_field(
        name="📢 Rule 3 — No Spam 🚯",
        value=(
            "Spam of any kind is not tolerated. **Do not spam or DM mentors, judges, or board.**\n"
            "**Includes:** mass pings, flooding, emote spam, or using @everyone/@here."
        ),
        inline=False,
    )
    .add_field(
        name="🧾 Additional Guidelines 📌",
        value=(
            "These rules are not exhaustive and may be updated at any time. If board member asks you to stop doing something, please comply. In addition, this Discord server follows:\n"
            "• [Discord Terms of Service](https://discord.com/terms) and [Community Guidelines](https://discord.com/guidelines)\n"
            "• [UIC Department of Computer Science Student Code of Conduct](https://www.cs.uic.edu/~grad/CS_Code_of_Conduct.pdf)\n"
            "• [SparkHacks Code of Conduct](https://outgoing-bubble-324.notion.site/Code-of-Conduct-2bdb7981cdc3815ba451eca455220dcd)"
        ),
        inline=False,
    )
    .add_field(
        name="✅🎉 Verification & Access 🎉",
        value=(
            "To gain full access to the server:\n"
            "1. **Read** all rules and guidelines above\n"
            "2. **Acknowledge and agree** to follow them\n"
            "3. **React** with ✅ under this message to gain access\n"
            "By reacting, you confirm that you understand and agree to follow all server rules."
        ),
        inline=False,
    )
)


# On Member Join
def WELCOME(member: discord.Member):
    return discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=f"Glad to see you here, {member.mention}!",
        color=colors.BOT,
    )


# Commands
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


# Audit Log
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
