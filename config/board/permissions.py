import discord

from config import permissions

BOARD = permissions.BASE | discord.Permissions(
    # General Server
    manage_emojis=True,
    # Text Channel
    mention_everyone=True,
    pin_messages=True,
    send_polls=True,
    # Events
    manage_events=True,
)
