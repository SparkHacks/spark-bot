import discord

# Unlike Permissions (a plain bitfield), PermissionOverwrite has three states per permission
# (allow/deny/neutral) and | isn't built in. So, here's my monkey patch for it:
# - Right operand's explicit values win
# - Neutral (None) entries are skipped
# - No type safety as it's lambda
discord.PermissionOverwrite.__or__ = (
    lambda self, other: discord.PermissionOverwrite(
        **{
            **{k: v for k, v in self if v is not None},
            **{k: v for k, v in other if v is not None},
        }
    )
)

DENY = discord.PermissionOverwrite(view_channel=False)

VIEW = discord.PermissionOverwrite(view_channel=True)

READ_ONLY = discord.PermissionOverwrite(
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

POLLS_ONLY = discord.PermissionOverwrite(
    # Text Channel
    send_messages=False,
    send_messages_in_threads=True,
    create_public_threads=True,
    send_polls=True,
)

THREADS_ONLY = discord.PermissionOverwrite(
    # Text Channel
    send_messages=False,
    send_messages_in_threads=True,
    create_public_threads=True,
)
