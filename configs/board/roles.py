import discord

from configs.board.permissions import (
    ADMIN_PERMISSIONS,
    BOARD_PERMISSIONS,
    LEAD_PERMISSIONS
)
from utils.dataclasses import Role

ROLES = [
    Role(
        name="Director",
        permissions=ADMIN_PERMISSIONS,
        color=discord.Color(int("#FFFFFF"[1:], 16))
    ),

    Role(
        name="Communications",
        permissions=BOARD_PERMISSIONS,
        color=discord.Color(int("#E91E63"[1:], 16))
    ),
    Role(
        name="Design",
        color=discord.Color(int("#FFFF00"[1:], 16))
    ),
    Role(
        name="Experience",
        color=discord.Color(int("#FF00FF"[1:], 16))
    ),
    Role(
        name="Logistics",
        color=discord.Color(int("#3498DB"[1:], 16))
    ),
    Role(
        name="Media",
        color=discord.Color(int("#57F287"[1:], 16))
    ),
    Role(
        name="Webdev",
        color=discord.Color(int("#9C00EB"[1:], 16))
    ),

    Role(
        name="Lead",
        permissions=LEAD_PERMISSIONS,
        color=discord.Color(int("#95A5A6"[1:], 16))
    ),
    Role(
        name="Board",
        permissions=BOARD_PERMISSIONS,
        color=discord.Color(int("#607D8B"[1:], 16))
    ),
]
