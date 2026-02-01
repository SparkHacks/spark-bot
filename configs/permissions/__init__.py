import discord

DEFAULT = discord.Permissions(
    # Membership Permissions
    change_nickname=True,
    # Text Channel Permissions
    add_reactions=True,
    use_external_emojis=True,
    read_message_history=True,
)

BOARD = discord.Permissions(
    # General server permissons
    manage_emojis=True,
    # Membership Permissions
    manage_nicknames=True,
    kick_members=True,
    ban_members=True,
    moderate_members=True,
    # Text Channel Permissions
    mention_everyone=True,
    manage_messages=True,
    pin_messages=True,
    # Voice Channels Permissions
    use_voice_activation=True,
    priority_speaker=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    set_voice_channel_status=True,
    # Events Permissions
    manage_events=True,
)

ADMIN = discord.Permissions(administrator=True)
