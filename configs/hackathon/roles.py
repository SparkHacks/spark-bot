import discord

from configs import permissions
from utils.dataclasses import Role, RoleCategory

EVERYONE_ROLE = Role(name="@everyone")

BOARD_ROLE = Role(
    name="Board",
    permissions=permissions.BOARD,
    color="#F1CC8D",
    hoist=True,
)
SPONSOR_ROLE = Role(name="Sponsor", color="#F8AAFF", hoist=True)
JUDGE_ROLE = Role(name="Judge", color="#FCA129", hoist=True)
MENTOR_ROLE = Role(name="Mentor", color="#0F218A", hoist=True)
HACKER_ROLE = Role(name="Hacker", color="#F1C40F", hoist=True)

PERSONAL_ROLE_CATEGORY = RoleCategory(name="Personal")
EXPERIENCE_ROLE_CATEGORY = RoleCategory(name="Experience")
TEAM_STATUS_ROLE_CATEGORY = RoleCategory(name="Team Status")

ROLES = [
    Role(
        name="Director",
        permissions=permissions.ADMIN,
        color="#7A0008",
        hoist=True,
    ),
    BOARD_ROLE,
    SPONSOR_ROLE,
    JUDGE_ROLE,
    MENTOR_ROLE,
    HACKER_ROLE,
    PERSONAL_ROLE_CATEGORY,
    Role(name="Freshman", color=discord.Color.teal()),
    Role(name="Sophomore", color=discord.Color.green()),
    Role(name="Junior", color=discord.Color.blue()),
    Role(name="Senior", color=discord.Color.purple()),
    Role(name="Master", color=discord.Color.fuchsia()),
    Role(name="He/Him", color="#99AAB5"),
    Role(name="She/Her", color="#99AAB5"),
    Role(name="They/Them", color="#99AAB5"),
    Role(name="Any Pronouns", color="#99AAB5"),
    Role(name="Ask My Pronouns", color="#99AAB5"),
    EXPERIENCE_ROLE_CATEGORY,
    Role(name="First-Time Hacker", color=discord.Color.green()),
    Role(name="Experienced Hacker", color=discord.Color.blue()),
    Role(name="New Attendee", color=discord.Color.purple()),
    Role(name="Returning Attendee", color=discord.Color.fuchsia()),
    TEAM_STATUS_ROLE_CATEGORY,
    Role(name="Looking for Team", color=discord.Color.yellow()),
    Role(name="Looking for Members", color=discord.Color.orange()),
    Role(name="Teamed Up", color=discord.Color.green()),
    Role(name="Bots", color="#607D8B", hoist=True),
]
