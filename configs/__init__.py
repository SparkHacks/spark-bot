import discord

BASE_PERMISSIONS = discord.Permissions(
    # General Server Permissions
    view_channel=True,

    # Membership Permissions
    change_nickname=True,

    # Text Channel Permissions
    send_messages=True,
    send_messages_in_threads=True,
    create_public_threads=True,
    embed_links=True,
    attach_files=True,
    add_reactions=True,
    use_external_emojis=True,
    use_external_stickers=True,
    read_message_history=True,

    # Voice Channels Permissions
    connect=True,
    speak=True,
    stream=True,
    use_voice_activation=True,

    # Apps Permissions
    use_application_commands=True
)