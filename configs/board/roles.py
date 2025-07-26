import discord

from configs.board.permissions import (
    ADMIN_PERMISSIONS,
    BOARD_PERMISSIONS,
    LEAD_PERMISSIONS
)
from utils.dataclasses import Role

BOT_ROLE = Role(
    name="SparkHacks Bot",
    permissions=ADMIN_PERMISSIONS,
    color=discord.Color(int("#A5A8C3"[1:], 16)),
    hoist=True
)

LEAD_ROLE = Role(
    name="Lead",
    permissions=LEAD_PERMISSIONS,
    color=discord.Color(int("#9E9E9E"[1:], 16))
)
BOARD_ROLE = Role(
    name="Board",
    permissions=BOARD_PERMISSIONS,
    color=discord.Color(int("#A97142"[1:], 16))
)

ROLES = [
    Role(
        name="Director",
        permissions=ADMIN_PERMISSIONS,
        color=discord.Color(int("#B29535"[1:], 16)),
        hoist=True
    ),

    Role(
        name="Communications",
        color=discord.Color(int("#E91E63"[1:], 16)),
        hoist=True
    ),
    Role(
        name="Design",
        color=discord.Color(int("#57F287"[1:], 16)),
        hoist=True
    ),
    Role(
        name="Experience",
        color=discord.Color(int("#EB459E"[1:], 16)),
        hoist=True
    ),
    Role(
        name="Logistics",
        color=discord.Color(int("#E67E22"[1:], 16)),
        hoist=True
    ),
    Role(
        name="Media",
        color=discord.Color(int("#3498DB"[1:], 16)),
        hoist=True
    ),
    Role(
        name="Webdev",
        color=discord.Color(int("#9C00EB"[1:], 16)),
        hoist=True
    ),

    LEAD_ROLE,
    BOARD_ROLE
]
