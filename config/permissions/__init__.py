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

ADMIN = discord.Permissions(administrator=True)
