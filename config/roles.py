from config import permissions
from static import colors
from util.dataclasses import Role

EVERYONE = Role(name="@everyone")

BOTS = Role(name="Bots", color=colors.BOTS, hoist=True)

DIRECTOR = Role(
    name="Director",
    permissions=permissions.ADMIN,
    color=colors.DIRECTOR,
    hoist=True,
)
