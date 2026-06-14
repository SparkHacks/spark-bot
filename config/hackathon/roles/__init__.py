import discord

from config import permissions, roles
from utils.dataclasses import Role

from . import categories

SPONSOR = Role(
    name="Sponsor", permissions=permissions.BASE, color="#F8AAFF", hoist=True
)
JUDGE = Role(
    name="Judge", permissions=permissions.BASE, color="#FCA129", hoist=True
)
MENTOR = Role(
    name="Mentor", permissions=permissions.BASE, color="#0F218A", hoist=True
)
HACKER = Role(
    name="Hacker", permissions=permissions.BASE, color="#F1C40F", hoist=True
)

ROLES = [
    roles.DIRECTOR,
    roles.BOARD,
    SPONSOR,
    JUDGE,
    MENTOR,
    HACKER,
    categories.PERSONAL,
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
    categories.EXPERIENCE,
    Role(name="First-Time Hacker", color=discord.Color.green()),
    Role(name="Experienced Hacker", color=discord.Color.blue()),
    Role(name="New Attendee", color=discord.Color.purple()),
    Role(name="Returning Attendee", color=discord.Color.fuchsia()),
    categories.TEAM_STATUS,
    Role(name="Looking for Team", color=discord.Color.yellow()),
    Role(name="Looking for Members", color=discord.Color.orange()),
    Role(name="Teamed Up", color=discord.Color.green()),
    Role(name="Bots", color="#607D8B", hoist=True),
]
