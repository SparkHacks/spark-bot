import discord

from config import permissions

BOARD = permissions.BASE | discord.Permissions(
    # General Server
    manage_channels=True,
    manage_roles=True,
    manage_emojis=True,
    # Membership
    manage_nicknames=True,
    kick_members=True,
    ban_members=True,
    moderate_members=True,
    # Text Channel
    mention_everyone=True,
    manage_messages=True,
    pin_messages=True,
    manage_threads=True,
    send_polls=True,
    # Voice Channel
    priority_speaker=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    set_voice_channel_status=True,
    # Events
    manage_events=True,
)
