from configs.hackathon.roles import HACKER, JUDGE, MENTOR, SPONSOR
from configs.permissions.overwrites import DENY, READ_ONLY, READ_WRITE
from utils.dataclasses import Category, Channel

WELCOME_CHANNEL_NAME = "🎉welcome👋"
RULES_CHANNEL_NAME = "📜rules⚖️"

CHANNELS = [
    Channel(name=WELCOME_CHANNEL_NAME),
    Channel(name=RULES_CHANNEL_NAME),
    Category(
        name="🗞 Spark Hub 📰",
        channels=[
            Channel(
                name="🚨fire🔥",
                type="text",
                overwrites={
                    SPONSOR: DENY,
                    JUDGE: DENY,
                    MENTOR: DENY,
                },
            ),
            Channel(
                name="💬board-chat🧠",
                type="text",
                overwrites={
                    SPONSOR: DENY,
                    JUDGE: DENY,
                    MENTOR: DENY,
                },
            ),
            Channel(
                name="🤝sponsor-chat💼",
                type="text",
                overwrites={
                    SPONSOR: READ_WRITE,
                    JUDGE: DENY,
                    MENTOR: DENY,
                },
            ),
            Channel(
                name="⚖️judge-chat🧑‍⚖️",
                type="text",
                roles=[JUDGE],
                overwrites={
                    SPONSOR: DENY,
                    JUDGE: READ_WRITE,
                    MENTOR: DENY,
                },
            ),
            Channel(
                name="🧑‍🏫mentor-chat💡",
                type="text",
                overwrites={
                    SPONSOR: DENY,
                    JUDGE: DENY,
                    MENTOR: READ_WRITE,
                },
            ),
        ],
        overwrites={
            SPONSOR: READ_ONLY,
            JUDGE: READ_ONLY,
            MENTOR: READ_ONLY,
        },
    ),
    Category(
        name="📢 Info Hub 📚",
        channels=[
            Channel(name="📢announcements🚨", type="text"),
            Channel(name="📚resources🤓", type="text"),
        ],
        overwrites={
            SPONSOR: READ_ONLY,
            JUDGE: READ_ONLY,
            MENTOR: READ_ONLY,
            HACKER: READ_ONLY,
        },
    ),
    Category(
        name="👋 Introductions 🧩",
        channels=[
            Channel(
                name="🏗️board-introductions🧠",
                type="text",
            ),
            Channel(
                name="⚖️judge-and-mentor-introductions🧑‍🏫",
                type="text",
                overwrites={
                    JUDGE: READ_WRITE,
                    MENTOR: READ_WRITE,
                },
            ),
            Channel(
                name="💻hacker-introductions🚀",
                type="text",
                overwrites={HACKER: READ_WRITE},
            ),
        ],
        overwrites={
            SPONSOR: READ_ONLY,
            JUDGE: READ_ONLY,
            MENTOR: READ_ONLY,
            HACKER: READ_ONLY,
        },
    ),
    Category(
        name="🗞 Hackers Hub 👨‍💻",
        channels=[
            Channel(name="💬general💼", type="text"),
            Channel(name="💬yapping🗣️", type="text"),
            Channel(name="😂memes🗿", type="text"),
            Channel(name="📷photo-dump🎞️", type="text"),
        ],
        overwrites={
            SPONSOR: READ_WRITE,
            JUDGE: READ_WRITE,
            MENTOR: READ_WRITE,
            HACKER: READ_WRITE,
        },
    ),
    Category(
        name="🛠️ Support Hub 🆘",
        channels=[
            Channel(name="🤝looking-for-a-team🔍", type="forum"),
            Channel(name="❓ask-sparkhacks📣", type="forum"),
            Channel(name="🧑‍🏫ask-a-mentor💬", type="forum"),
        ],
        overwrites={
            SPONSOR: READ_WRITE,
            JUDGE: READ_WRITE,
            MENTOR: READ_WRITE,
            HACKER: READ_WRITE,
        },
    ),
    Category(
        name="🎤 Voice Chats 🎧",
        channels=[
            Channel(name="🛋️spark-lounge💬", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-1🎙️", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-2🎙️", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-3🎙️", type="voice"),
        ],
        overwrites={
            SPONSOR: READ_WRITE,
            JUDGE: READ_WRITE,
            MENTOR: READ_WRITE,
            HACKER: READ_WRITE,
        },
    ),
    Category(
        name="🤖 Bots Hub ⚙️",
        channels=[
            Channel(name="commands", type="text"),
            Channel(name="sys-logs", type="text"),
            Channel(name="bot-logs", type="text"),
            Channel(name="mod-logs", type="text"),
            Channel(name="member-logs", type="text"),
            Channel(name="message-logs", type="text"),
            Channel(name="server-logs", type="text"),
        ],
    ),
]
