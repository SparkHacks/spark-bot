import discord

DENY = discord.PermissionOverwrite(view_channel=False)

READ_ONLY = discord.PermissionOverwrite(
    # General server permissons
    view_channel=True,
)

READ_WRITE = discord.PermissionOverwrite(
    # General server permissons
    view_channel=True,
    # Text Channel Permissions
    send_messages=True,
    embed_links=True,
    attach_files=True,
    use_external_stickers=True,
    # Voice Channels Permissions
    connect=True,
    speak=True,
    stream=True,
    # Apps Permissions
    use_application_commands=True,
)
