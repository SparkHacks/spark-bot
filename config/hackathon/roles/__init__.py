from config import permissions, roles
from config.hackathon.roles import categories
from static import colors
from utils.dataclasses import Role

SPONSOR = Role(
    name="Sponsor",
    permissions=permissions.BASE,
    color=colors.SPONSOR,
    hoist=True,
)
MENTOR = Role(
    name="Mentor",
    permissions=permissions.BASE,
    color=colors.MENTOR,
    hoist=True,
)
HACKER = Role(
    name="Hacker",
    permissions=permissions.BASE,
    color=colors.HACKER,
    hoist=True,
)

ROLES = [
    roles.DIRECTOR,
    roles.BOARD,
    SPONSOR,
    MENTOR,
    HACKER,
    categories.PERSONAL,
    Role(name="Freshman", color=colors.FRESHMAN),
    Role(name="Sophomore", color=colors.SOPHOMORE),
    Role(name="Junior", color=colors.JUNIOR),
    Role(name="Senior", color=colors.SENIOR),
    Role(name="Master", color=colors.MASTER),
    Role(name="He/Him", color=colors.PRONOUNS),
    Role(name="She/Her", color=colors.PRONOUNS),
    Role(name="They/Them", color=colors.PRONOUNS),
    Role(name="Any Pronouns", color=colors.PRONOUNS),
    Role(name="Ask My Pronouns", color=colors.PRONOUNS),
    categories.EXPERIENCE,
    Role(name="First-Time Hacker", color=colors.FIRST_TIME_HACKER),
    Role(name="Experienced Hacker", color=colors.EXPERIENCED_HACKER),
    Role(name="New Attendee", color=colors.NEW_ATTENDEE),
    Role(name="Returning Attendee", color=colors.RETURNING_ATTENDEE),
    categories.TEAM_STATUS,
    Role(name="Looking for Team", color=colors.LOOKING_FOR_TEAM),
    Role(name="Looking for Members", color=colors.LOOKING_FOR_MEMBERS),
    Role(name="Teamed Up", color=colors.TEAMED_UP),
]
