from configs import permissions
from utils.dataclasses import Role

BOARD = Role(
    name="Board",
    permissions=permissions.BOARD,
    hex_color="#F1CC8D",
    hoist=True,
)

SPONSOR = Role(name="Sponsor", hex_color="#F8AAFF", hoist=True)

JUDGE = Role(name="Judge", hex_color="#FCA129", hoist=True)

MENTOR = Role(name="Mentor", hex_color="#0F218A", hoist=True)

HACKER = Role(name="Hacker", hex_color="#F1C40F", hoist=True)

ROLES = [
    Role(
        name="Director",
        permissions=permissions.ADMIN,
        hex_color="#7A0008",
        hoist=True,
    ),
    BOARD,
    SPONSOR,
    JUDGE,
    MENTOR,
    HACKER,
    Role(name="Bots", hex_color="#607D8B", hoist=True),
]
