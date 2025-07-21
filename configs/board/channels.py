from utils.dataclasses import Category, Channel

CHANNELS = [
    Channel(name="🎉welcome👋", type="text")
]

CATEGORIES = [
    Category(
        name="🗞 Hub 📰",
        channels=[
            Channel(name="📢announcements🚨", type="text"),
            Channel(name="💬general💼",       type="text"),
            Channel(name="🗳️polls📊",         type="text"),
            Channel(name="💡suggestions📝",   type="text"),
            Channel(name="📷photos🎞️",        type="text"),
            Channel(name="📚resources🤓",     type="text"),
        ]
    ),
    Category(
        name="🤪 Unserious 🎉",
        channels=[
            Channel(name="💬yapping🗣️", type="text"),
            Channel(name="😂memes🗿",   type="text"),
        ]
    ),
    Category(
        name="💪 Leads 👑",
        channels=[
            Channel(name="💼discussion📈", type="text"),
            Channel(name="💼leads-vc🎧", type="voice"),
        ]
    ),
    Category(
        name="💼 Teams 🤝",
        channels=[
            Channel(name="💵communications📢", type="text"),
            Channel(name="🎨design🪄",         type="text"),
            Channel(name="💃experience✨",     type="text"),
            Channel(name="📦logistics📈",      type="text"),
            Channel(name="📱media📸",          type="text"),
            Channel(name="💻webdev👾",         type="text"),
        ]
    ),
    Category(
        name="🎤 Voice Chats 🎧",
        channels=[
            Channel(name="🥱lounge😴",            type="voice"),
            Channel(name="💵communications-vc🎧", type="voice"),
            Channel(name="🎨design-vc🎧",         type="voice"),
            Channel(name="💃experience-vc🎧",     type="voice"),
            Channel(name="📦logistics-vc🎧",      type="voice"),
            Channel(name="📱media-vc🎧",          type="voice"),
            Channel(name="💻webdev-vc🎧",         type="voice"),
        ]
    ),
    Category(
        name="🤖 SparkHacks Bot ⚙️",
        channels=[
            Channel(name="💬commands🛠️", type="text"),
            Channel(name="📊logs📈",     type="text"),
        ]
    ),
]
