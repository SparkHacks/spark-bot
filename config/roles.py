from config import permissions
from static import colors
from utils.dataclasses import Role

EVERYONE = Role(name="@everyone")

BOARD = Role(
    name="Board",
    permissions=permissions.BOARD,
    color=colors.BOARD,
    hoist=True,
)

BOTDEV = Role(
    name="BotDev",
    permissions=permissions.ADMIN,
    color=colors.BOTDEV,
    hoist=True,
)

DIRECTOR = Role(
    name="Director",
    permissions=permissions.ADMIN,
    color=colors.DIRECTOR,
    hoist=True,
)
