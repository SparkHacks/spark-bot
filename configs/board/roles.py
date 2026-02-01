from configs.board.permissions import (
    ADMIN_PERMISSIONS,
    BOARD_PERMISSIONS,
    LEAD_PERMISSIONS,
)
from utils.dataclasses import Role

LEAD_ROLE = Role(name="Lead", permissions=LEAD_PERMISSIONS, color="#9E9E9E")
BOARD_ROLE = Role(name="Board", permissions=BOARD_PERMISSIONS, color="#A97142")

ROLES = [
    Role(
        name="Director",
        permissions=ADMIN_PERMISSIONS,
        color="#B29535",
        hoist=True,
    ),
    Role(name="Communications", color="#E91E63", hoist=True),
    Role(name="Experience", color="#EB459E", hoist=True),
    Role(name="Logistics", color="#E67E22", hoist=True),
    Role(name="Outreach", color="#3498DB", hoist=True),
    Role(name="WebDev", color="#9C00EB", hoist=True),
    LEAD_ROLE,
    BOARD_ROLE,
    Role(name="Bots", color="#607D8B", hoist=True),
]
