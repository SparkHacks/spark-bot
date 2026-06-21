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

ALUMNI = Role(
    name="Alumni",
    permissions=permissions.ADMIN,
    color=colors.ALUMNI,
)

DIRECTOR = Role(
    name="Director",
    permissions=permissions.ADMIN,
    color=colors.DIRECTOR,
    hoist=True,
)
