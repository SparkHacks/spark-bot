import discord

from config.permissions import overwrites  # noqa: F401

EVERYONE = discord.Permissions(
    # Membership
    change_nickname=True,
    # Text Channel
    add_reactions=True,
    use_external_emojis=True,
    read_message_history=True,
)

BASE = discord.Permissions(
    # General Server
    view_channel=True,
    # Text Channel
    send_messages=True,
    send_messages_in_threads=True,
    create_public_threads=True,
    embed_links=True,
    attach_files=True,
    # Voice Channel
    connect=True,
    speak=True,
    stream=True,
    use_voice_activation=True,
    # Apps
    use_application_commands=True,
)

BOARD = BASE | discord.Permissions(
    # General Server
    manage_channels=True,
    manage_roles=True,
    manage_emojis=True,
    view_audit_log=True,
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

ADMIN = discord.Permissions(administrator=True)
