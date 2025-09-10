from configs.board.permissions import (
    ADMIN_PERMISSIONS, 
    BOARD_PERMISSIONS,
    LEAD_PERMISSIONS
)
from utils.dataclasses import Role

BOT_ROLE = Role(
    name="SparkHacks Bot", permissions=ADMIN_PERMISSIONS, hex_color="#A5A8C3"
)

LEAD_ROLE = Role(
    name="Lead", permissions=LEAD_PERMISSIONS, hex_color="#9E9E9E"
)
BOARD_ROLE = Role(
    name="Board", permissions=BOARD_PERMISSIONS, hex_color="#A97142"
)

ROLES = [
    Role(
        name="Director",
        permissions=ADMIN_PERMISSIONS,
        hex_color="#B29535",
        hoist=True,
    ),
    Role(name="Communications", hex_color="#E91E63", hoist=True),
    Role(name="Experience", hex_color="#EB459E", hoist=True),
    Role(name="Logistics", hex_color="#E67E22", hoist=True),
    Role(name="Outreach", hex_color="#3498DB", hoist=True),
    Role(name="Webdev", hex_color="#9C00EB", hoist=True),
    LEAD_ROLE,
    BOARD_ROLE,
    Role(name="Bots", hex_color="#607D8B", hoist=True),
]
