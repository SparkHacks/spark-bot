import discord

from . import overwrites  # noqa: F401

EVERYONE = discord.Permissions(
    # Membership
    change_nickname=True,
    # Text
    add_reactions=True,
    use_external_emojis=True,
    read_message_history=True,
)

BASE = discord.Permissions(
    # Membership
    change_nickname=True,
    # Text
    send_messages=True,
    send_messages_in_threads=True,
    create_public_threads=True,
    embed_links=True,
    attach_files=True,
    add_reactions=True,
    use_external_emojis=True,
    use_external_stickers=True,
    read_message_history=True,
    # Voice
    connect=True,
    speak=True,
    stream=True,
    use_voice_activation=True,
    # Apps
    use_application_commands=True,
)

BOARD = discord.Permissions(
    # Membership
    change_nickname=True,
    manage_nicknames=True,
    # Text
    send_messages=True,
    send_messages_in_threads=True,
    create_public_threads=True,
    embed_links=True,
    attach_files=True,
    add_reactions=True,
    use_external_emojis=True,
    use_external_stickers=True,
    read_message_history=True,
    mention_everyone=True,
    manage_messages=True,
    pin_messages=True,
    send_voice_messages=True,
    send_polls=True,
    # Voice
    connect=True,
    speak=True,
    stream=True,
    use_voice_activation=True,
    priority_speaker=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    set_voice_channel_status=True,
    # Server management (channels and expressions only, not roles/permissions)
    manage_channels=True,
    view_audit_log=True,
    # Events
    manage_events=True,
    # Moderation
    kick_members=True,
    moderate_members=True,
)

ADMIN = discord.Permissions(administrator=True)
