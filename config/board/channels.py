from config import board, permissions, roles
from util.dataclasses import ChannelCategory, TextChannel, VoiceChannel

WELCOME = TextChannel(
    name="🎉welcome👋",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)

INTRODUCTIONS = TextChannel(
    name="🗣introductions😎",
    topic="Introduce yourself! Share your name, major, year, and hobbies/interests!",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_WRITE},
)

LOGS = TextChannel(
    name="📊logs📈",
    topic="Nothing to see here.",
    overwrites={board.roles.BOARD: permissions.overwrites.READ_ONLY},
)

CHANNELS = [
    WELCOME,
    INTRODUCTIONS,
    ChannelCategory(
        name="🗞 Hub 📰",
        channels=[
            TextChannel(
                name="📢announcements🚨",
                topic="Never mute this one. Seriously.",
                overwrites={board.roles.BOARD: permissions.overwrites.THREADS_ONLY},
            ),
            TextChannel(name="💬general💼", topic="The water cooler."),
            TextChannel(name="🗳️polls📊", topic="Democracy time."),
            TextChannel(name="💡suggestions📝", topic="Got an idea? Drop it here!"),
            TextChannel(name="📷photos🎞️", topic="Share your SparkHacks memories!"),
            TextChannel(name="📚resources🤓", topic="Temu Confluence."),
        ],
    ),
    ChannelCategory(
        name="🤪 Unserious 🎉",
        channels=[
            TextChannel(name="💬yapping🗣️", topic="Off-topic. No work here."),
            TextChannel(name="😂memes🗿", topic="The culture."),
        ],
    ),
    ChannelCategory(
        name="💪 Leads 👑",
        channels=[
            TextChannel(name="💼discussion📈", topic="Leads-only safe space."),
            VoiceChannel(name="💼leads-vc🎧"),
        ],
        overwrites={
            board.roles.BOARD: permissions.overwrites.DENY,
            board.roles.LEAD: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="💼 Teams 🤝",
        channels=[
            TextChannel(
                name="💵communications📢", topic="Sliding into inboxes since 2022."
            ),
            TextChannel(
                name="🎨design✨", topic="Making it pretty, so you don't have to."
            ),
            TextChannel(name="💃experience✨", topic="Vibes are our product."),
            TextChannel(
                name="📦logistics📈",
                topic="If it's not in the spreadsheet, it doesn't exist.",
            ),
            TextChannel(name="📸media🎞️", topic="Capturing the chaos."),
            TextChannel(name="💻webdev👾", topic="404: sleep not found."),
        ],
    ),
    ChannelCategory(
        name="🎤 Voice Chats 🎧",
        channels=[
            VoiceChannel(name="🥱lounge😴"),
            VoiceChannel(name="💵communications-vc🎧"),
            VoiceChannel(name="🎨design-vc✨"),
            VoiceChannel(name="💃experience-vc🎧"),
            VoiceChannel(name="📦logistics-vc🎧"),
            VoiceChannel(name="📸media-vc🎞️"),
            VoiceChannel(name="💻webdev-vc🎧"),
        ],
    ),
    ChannelCategory(
        name="🤖 SparkHacks Bot ⚙️",
        channels=[
            TextChannel(name="💬commands🛠️", topic="Bother the bot here."),
            LOGS,
        ],
    ),
]
