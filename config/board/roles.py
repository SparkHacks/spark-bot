from config import roles
from static import colors
from utils.dataclasses import Role

LEAD = Role(name="Lead", color=colors.LEAD, hoist=True)

ROLES = [
    roles.DIRECTOR,
    roles.ALUMNI,
    LEAD,
    Role(name="Communications", color=colors.COMMUNICATIONS, hoist=True),
    Role(name="Experience", color=colors.EXPERIENCE, hoist=True),
    Role(name="Logistics", color=colors.LOGISTICS, hoist=True),
    Role(name="Outreach", color=colors.OUTREACH, hoist=True),
    Role(name="WebDev", color=colors.WEBDEV, hoist=True),
    roles.BOARD,
]
