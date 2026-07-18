import discord

DENY = discord.PermissionOverwrite(view_channel=False)

VIEW = discord.PermissionOverwrite(view_channel=True)

READ_ONLY = discord.PermissionOverwrite(
    # General
    view_channel=True,
    # Text Channel
    send_messages=False,
    send_messages_in_threads=False,
    create_public_threads=False,
    embed_links=False,
    attach_files=False,
    # Voice Channel
    connect=True,
    speak=False,
    stream=False,
)

READ_WRITE = discord.PermissionOverwrite(
    # General
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
)

THREADS_ONLY = discord.PermissionOverwrite(
    # General
    view_channel=True,
    # Text Channel
    send_messages=False,
    send_messages_in_threads=True,
    create_public_threads=True,
)
