from config import roles
from static import colors
from utils.dataclasses import Role

LEAD = Role(name="Lead", color=colors.LEAD, hoist=True)

ROLES = [
    roles.DIRECTOR,
    LEAD,
    roles.BOTDEV,
    Role(name="Communications", color=colors.COMMUNICATIONS, hoist=True),
    Role(name="Design", color=colors.DESIGN, hoist=True),
    Role(name="Experience", color=colors.EXPERIENCE, hoist=True),
    Role(name="Logistics", color=colors.LOGISTICS, hoist=True),
    Role(name="Media", color=colors.MEDIA, hoist=True),
    Role(name="WebDev", color=colors.WEBDEV, hoist=True),
    roles.BOARD,
]
