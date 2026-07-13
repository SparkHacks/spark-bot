from config import hackathon, permissions, roles
from utils.dataclasses import Channel, ChannelCategory

WELCOME = Channel(
    name="🎉welcome👋",
    overwrites={
        roles.EVERYONE: permissions.overwrites.VIEW | permissions.overwrites.READ_ONLY
    },
)

RULES = Channel(
    name="📜rules⚖️",
    overwrites={
        roles.EVERYONE: permissions.overwrites.VIEW | permissions.overwrites.READ_ONLY
    },
)

SYS_LOGS = Channel(name="🖥️sys-logs⚙️")
MOD_LOGS = Channel(name="🛡️mod-logs🔨")
GATEWAY_LOGS = Channel(name="🚪gateway-logs🔑")
MEMBER_LOGS = Channel(name="👥member-logs📋")
MESSAGE_LOGS = Channel(name="💬message-logs📝")

CHANNELS = [
    WELCOME,
    RULES,
    Channel(
        name="🗣introductions✨",
        overwrites={
            roles.EVERYONE: permissions.overwrites.VIEW
            | permissions.overwrites.READ_WRITE
        },
    ),
    ChannelCategory(
        name="🗞 Spark Hub 📰",
        channels=[
            Channel(name="🚨fire🔥"),
            Channel(name="💬board-chat🧠"),
            Channel(
                name="🤝sponsor-chat💼",
                overwrites={hackathon.roles.SPONSOR: permissions.overwrites.VIEW},
            ),
            Channel(
                name="🧑‍🏫mentor-chat💡",
                overwrites={hackathon.roles.MENTOR: permissions.overwrites.VIEW},
            ),
        ],
    ),
    ChannelCategory(
        name="📢 Info Hub 📚",
        channels=[
            Channel(name="📢announcements🚨", type="announcement"),
            Channel(name="📚resources🤓"),
        ],
        overwrites={
            roles.EVERYONE: permissions.overwrites.VIEW
            | permissions.overwrites.READ_ONLY,
            roles.BOARD: permissions.overwrites.VIEW
            | permissions.overwrites.READ_WRITE,
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
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.SPONSOR: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
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
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.SPONSOR: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
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
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="🤖 Bots Hub ⚙️",
        channels=[
            Channel(name="💬commands🛠️"),
            SYS_LOGS,
            MOD_LOGS,
            GATEWAY_LOGS,
            MEMBER_LOGS,
            MESSAGE_LOGS,
            Channel(name="🗄️server-logs📜"),
        ],
    ),
]
