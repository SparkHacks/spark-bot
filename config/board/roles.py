from config import roles
from utils.dataclasses import Role

LEAD = Role(name="Lead", color="#9E9E9E", hoist=True)

ROLES = [
    roles.DIRECTOR,
    LEAD,
    Role(name="Communications", color="#E91E63", hoist=True),
    Role(name="Experience", color="#EB459E", hoist=True),
    Role(name="Logistics", color="#E67E22", hoist=True),
    Role(name="Outreach", color="#3498DB", hoist=True),
    Role(name="WebDev", color="#9C00EB", hoist=True),
    roles.BOARD,
    Role(name="Bots", color="#607D8B", hoist=True),
]
