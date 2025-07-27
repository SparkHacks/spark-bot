import discord 

from configs.permissions import BASE_PERMISSIONS

BOARD_PERMISSIONS = discord.Permissions(permissions=BASE_PERMISSIONS.value)
BOARD_PERMISSIONS.update(
    # General Server Permissions
    create_expressions=True,
    manage_expressions=True,

    # Text Channel Permissions
    mention_everyone=True,
    send_voice_messages=True,
    send_polls=True,

    # Events Permissions
    create_events=True,
    manage_events=True
)

LEAD_PERMISSIONS = discord.Permissions(permissions=BOARD_PERMISSIONS.value)
LEAD_PERMISSIONS.update(
    # General Server Permissions
    manage_channels=True,

    # Voice Channels Permissions
    mute_members=True,
    move_members=True
)

ADMIN_PERMISSIONS = discord.Permissions(administrator=True)