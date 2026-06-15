from config import hackathon, permissions, roles
from utils.dataclasses import Channel, ChannelCategory

WELCOME = Channel(
    name="🎉welcome👋",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)
RULES = Channel(
    name="📜rules⚖️",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)

CHANNELS = [
    WELCOME,
    RULES,
    Channel(
        name="🗣introductions✨",
        overwrites={roles.EVERYONE: permissions.overwrites.READ_WRITE},
    ),
    ChannelCategory(
        name="🗞 Spark Hub 📰",
        channels=[
            Channel(
                name="🚨fire🔥",
                overwrites={
                    hackathon.roles.SPONSOR: permissions.overwrites.DENY,
                    hackathon.roles.JUDGE: permissions.overwrites.DENY,
                    hackathon.roles.MENTOR: permissions.overwrites.DENY,
                },
            ),
            Channel(
                name="💬board-chat🧠",
                overwrites={
                    hackathon.roles.SPONSOR: permissions.overwrites.DENY,
                    hackathon.roles.JUDGE: permissions.overwrites.DENY,
                    hackathon.roles.MENTOR: permissions.overwrites.DENY,
                },
            ),
            Channel(
                name="🤝sponsor-chat💼",
                overwrites={
                    hackathon.roles.SPONSOR: permissions.overwrites.READ_WRITE,
                    hackathon.roles.JUDGE: permissions.overwrites.DENY,
                    hackathon.roles.MENTOR: permissions.overwrites.DENY,
                },
            ),
            Channel(
                name="⚖️judge-chat🧑‍⚖️",
                overwrites={
                    hackathon.roles.SPONSOR: permissions.overwrites.DENY,
                    hackathon.roles.JUDGE: permissions.overwrites.READ_WRITE,
                    hackathon.roles.MENTOR: permissions.overwrites.DENY,
                },
            ),
            Channel(
                name="🧑‍🏫mentor-chat💡",
                overwrites={
                    hackathon.roles.SPONSOR: permissions.overwrites.DENY,
                    hackathon.roles.JUDGE: permissions.overwrites.DENY,
                    hackathon.roles.MENTOR: permissions.overwrites.READ_WRITE,
                },
            ),
        ],
        overwrites={
            hackathon.roles.SPONSOR: permissions.overwrites.READ_ONLY,
            hackathon.roles.JUDGE: permissions.overwrites.READ_ONLY,
            hackathon.roles.MENTOR: permissions.overwrites.READ_ONLY,
        },
    ),
    ChannelCategory(
        name="📢 Info Hub 📚",
        channels=[
            Channel(name="📢announcements🚨"),
            Channel(name="📚resources🤓"),
        ],
        overwrites={
            hackathon.roles.SPONSOR: permissions.overwrites.READ_ONLY,
            hackathon.roles.JUDGE: permissions.overwrites.READ_ONLY,
            hackathon.roles.MENTOR: permissions.overwrites.READ_ONLY,
            hackathon.roles.HACKER: permissions.overwrites.READ_ONLY,
            roles.EVERYONE: permissions.overwrites.READ_ONLY,
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
            hackathon.roles.SPONSOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.JUDGE: permissions.overwrites.READ_WRITE,
            hackathon.roles.MENTOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.HACKER: permissions.overwrites.READ_WRITE,
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
            hackathon.roles.SPONSOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.JUDGE: permissions.overwrites.READ_WRITE,
            hackathon.roles.MENTOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.HACKER: permissions.overwrites.READ_WRITE,
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
            hackathon.roles.SPONSOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.JUDGE: permissions.overwrites.READ_WRITE,
            hackathon.roles.MENTOR: permissions.overwrites.READ_WRITE,
            hackathon.roles.HACKER: permissions.overwrites.READ_WRITE,
        },
    ),
    ChannelCategory(
        name="🤖 Bots Hub ⚙️",
        channels=[
            Channel(name="commands"),
            Channel(name="sys-logs"),
            Channel(name="mod-logs"),
            Channel(name="member-logs"),
            Channel(name="message-logs"),
            Channel(name="server-logs"),
        ],
    ),
]
