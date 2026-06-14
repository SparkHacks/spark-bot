from config import permissions
from utils.dataclasses import Role

EVERYONE = Role(name="@everyone")
BOARD = Role(
    name="Board", permissions=permissions.BOARD, color="#F1CC8D", hoist=True
)
DIRECTOR = Role(
    name="Director", permissions=permissions.ADMIN, color="#7A0008", hoist=True
)
