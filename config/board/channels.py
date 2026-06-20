from config import board, permissions, roles
from utils.dataclasses import Channel, ChannelCategory

WELCOME = Channel(
    name="🎉welcome👋",
    overwrites={
        roles.EVERYONE: permissions.overwrites.VIEW
        | permissions.overwrites.READ_ONLY
    },
)

INTRODUCTIONS = Channel(
    name="🗣introductions😎",
    overwrites={
        roles.EVERYONE: permissions.overwrites.VIEW
        | permissions.overwrites.READ_WRITE
    },
)

LOGS = Channel(name="📊logs📈")

CHANNELS = [
    WELCOME,
    INTRODUCTIONS,
    ChannelCategory(
        name="🗞 Hub 📰",
        channels=[
            Channel(
                name="📢announcements🚨",
                overwrites={roles.BOARD: permissions.overwrites.THREADS_ONLY},
            ),
            Channel(name="💬general💼"),
            Channel(
                name="🗳️polls📊",
                overwrites={roles.BOARD: permissions.overwrites.POLLS_ONLY},
            ),
            Channel(name="💡suggestions📝"),
            Channel(name="📷photos🎞️"),
            Channel(name="📚resources🤓"),
        ],
    ),
    ChannelCategory(
        name="🤪 Unserious 🎉",
        channels=[
            Channel(name="💬yapping🗣️"),
            Channel(name="😂memes🗿"),
        ],
    ),
    ChannelCategory(
        name="💪 Leads 👑",
        channels=[
            Channel(name="💼discussion📈"),
            Channel(name="💼leads-vc🎧", type="voice"),
        ],
        overwrites={
            roles.BOARD: permissions.overwrites.DENY,
            board.roles.LEAD: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="💼 Teams 🤝",
        channels=[
            Channel(name="💵communications📢"),
            Channel(name="💃experience✨"),
            Channel(name="📦logistics📈"),
            Channel(name="📸outreach🎨"),
            Channel(name="💻webdev👾"),
        ],
    ),
    ChannelCategory(
        name="🎤 Voice Chats 🎧",
        channels=[
            Channel(name="🥱lounge😴", type="voice"),
            Channel(name="💵communications-vc🎧", type="voice"),
            Channel(name="💃experience-vc🎧", type="voice"),
            Channel(name="📦logistics-vc🎧", type="voice"),
            Channel(name="📸outreach-vc🎧", type="voice"),
            Channel(name="💻webdev-vc🎧", type="voice"),
        ],
    ),
    ChannelCategory(
        name="🤖 SparkHacks Bot ⚙️",
        channels=[
            Channel(name="💬commands🛠️"),
            LOGS,
        ],
    ),
]
