from configs.hackathon.roles import (
    EVERYONE_ROLE,
    HACKER_ROLE,
    JUDGE_ROLE,
    MENTOR_ROLE,
    SPONSOR_ROLE,
)
from configs.permissions.overwrites import DENY, READ_ONLY, READ_WRITE
from utils.dataclasses import Channel, ChannelCategory

WELCOME_CHANNEL_NAME = "🎉welcome👋"
RULES_CHANNEL_NAME = "📜rules⚖️"
INTRODUCTIONS_CHANNEL_NAME = "🗣introductions✨"

CHANNELS = [
    Channel(name=WELCOME_CHANNEL_NAME, overwrites={EVERYONE_ROLE: READ_ONLY}),
    Channel(name=RULES_CHANNEL_NAME, overwrites={EVERYONE_ROLE: READ_ONLY}),
    Channel(
        name=INTRODUCTIONS_CHANNEL_NAME, overwrites={EVERYONE_ROLE: READ_WRITE}
    ),
    ChannelCategory(
        name="🗞 Spark Hub 📰",
        channels=[
            Channel(
                name="🚨fire🔥",
                overwrites={
                    SPONSOR_ROLE: DENY,
                    JUDGE_ROLE: DENY,
                    MENTOR_ROLE: DENY,
                },
            ),
            Channel(
                name="💬board-chat🧠",
                overwrites={
                    SPONSOR_ROLE: DENY,
                    JUDGE_ROLE: DENY,
                    MENTOR_ROLE: DENY,
                },
            ),
            Channel(
                name="🤝sponsor-chat💼",
                overwrites={
                    SPONSOR_ROLE: READ_WRITE,
                    JUDGE_ROLE: DENY,
                    MENTOR_ROLE: DENY,
                },
            ),
            Channel(
                name="⚖️judge-chat🧑‍⚖️",
                roles=[JUDGE_ROLE],
                overwrites={
                    SPONSOR_ROLE: DENY,
                    JUDGE_ROLE: READ_WRITE,
                    MENTOR_ROLE: DENY,
                },
            ),
            Channel(
                name="🧑‍🏫mentor-chat💡",
                overwrites={
                    SPONSOR_ROLE: DENY,
                    JUDGE_ROLE: DENY,
                    MENTOR_ROLE: READ_WRITE,
                },
            ),
        ],
        overwrites={
            SPONSOR_ROLE: READ_ONLY,
            JUDGE_ROLE: READ_ONLY,
            MENTOR_ROLE: READ_ONLY,
        },
    ),
    ChannelCategory(
        name="📢 Info Hub 📚",
        channels=[
            Channel(name="📢announcements🚨"),
            Channel(name="📚resources🤓"),
        ],
        overwrites={
            SPONSOR_ROLE: READ_ONLY,
            JUDGE_ROLE: READ_ONLY,
            MENTOR_ROLE: READ_ONLY,
            HACKER_ROLE: READ_ONLY,
            EVERYONE_ROLE: READ_ONLY,
        },
    ),
    ChannelCategory(
        name="🗞 Hackers Hub 👨‍💻",
        channels=[
            Channel(name="💬general💼"),
            Channel(name="💬yapping🗣️"),
            Channel(name="😂memes🗿"),
            Channel(name="💼linkedin🔗"),
            Channel(name="📷photo-dump🎞️"),
        ],
        overwrites={
            SPONSOR_ROLE: READ_WRITE,
            JUDGE_ROLE: READ_WRITE,
            MENTOR_ROLE: READ_WRITE,
            HACKER_ROLE: READ_WRITE,
        },
    ),
    ChannelCategory(
        name="🛠️ Support Hub 🆘",
        channels=[
            Channel(name="🤝looking-for-a-team🔍", type="forum"),
            Channel(name="❓ask-sparkhacks📣", type="forum"),
            Channel(name="🤝ask-a-sponsor💼", type="forum"),
            Channel(name="🧑‍🏫ask-a-mentor💬", type="forum"),
        ],
        overwrites={
            SPONSOR_ROLE: READ_WRITE,
            JUDGE_ROLE: READ_WRITE,
            MENTOR_ROLE: READ_WRITE,
            HACKER_ROLE: READ_WRITE,
        },
    ),
    ChannelCategory(
        name="🎤 Voice Chats 🎧",
        channels=[
            Channel(name="🛋️spark-lounge💬", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-1🎙️", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-2🎙️", type="voice"),
            Channel(name="🧑‍🏫mentor-oh-3🎙️", type="voice"),
        ],
        overwrites={
            SPONSOR_ROLE: READ_WRITE,
            JUDGE_ROLE: READ_WRITE,
            MENTOR_ROLE: READ_WRITE,
            HACKER_ROLE: READ_WRITE,
        },
    ),
    ChannelCategory(
        name="🤖 Bots Hub ⚙️",
        channels=[
            Channel(name="commands"),
            Channel(name="sys-logs"),
            Channel(name="bot-logs"),
            Channel(name="mod-logs"),
            Channel(name="member-logs"),
            Channel(name="message-logs"),
            Channel(name="server-logs"),
        ],
    ),
]
