from config import permissions, roles
from utils.dataclasses import Channel, ChannelCategory

WELCOME = Channel(
    name="🎉welcome👋",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)
INTRODUCTIONS = Channel(name="🗣introductions😎")

CHANNELS = [
    WELCOME,
    INTRODUCTIONS,
    ChannelCategory(
        name="🗞 Hub 📰",
        channels=[
            Channel(name="📢announcements🚨", type="text"),
            Channel(name="💬general💼", type="text"),
            Channel(name="🗳️polls📊", type="text"),
            Channel(name="💡suggestions📝", type="text"),
            Channel(name="📷photos🎞️", type="text"),
            Channel(name="📚resources🤓", type="text"),
        ],
    ),
    ChannelCategory(
        name="🤪 Unserious 🎉",
        channels=[
            Channel(name="💬yapping🗣️", type="text"),
            Channel(name="😂memes🗿", type="text"),
        ],
    ),
    ChannelCategory(
        name="💪 Leads 👑",
        channels=[
            Channel(name="💼discussion📈", type="text"),
            Channel(name="💼leads-vc🎧", type="voice"),
        ],
    ),
    ChannelCategory(
        name="💼 Teams 🤝",
        channels=[
            Channel(name="💵communications📢", type="text"),
            Channel(name="💃experience✨", type="text"),
            Channel(name="📦logistics📈", type="text"),
            Channel(name="📸outreach🎨", type="text"),
            Channel(name="💻webdev👾", type="text"),
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
            Channel(name="💬commands🛠️", type="text"),
            Channel(name="📊logs📈", type="text"),
        ],
    ),
]
