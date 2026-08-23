import discord

from config import hackathon, permissions, roles
from util.dataclasses import ChannelCategory, ForumChannel, TextChannel, VoiceChannel

WELCOME = TextChannel(
    name="🎉welcome👋",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)

RULES = TextChannel(
    name="📜rules⚖️",
    topic="React with ✅ to accept the rules and unlock the server.",
    overwrites={roles.EVERYONE: permissions.overwrites.READ_ONLY},
)

SYS_LOGS = TextChannel(
    name="🖥️sys-logs⚙️",
    topic="Bot status and events.",
    overwrites={hackathon.roles.BOARD: permissions.overwrites.READ_ONLY},
)
MOD_LOGS = TextChannel(
    name="🛡️mod-logs🔨",
    topic="Bans, kicks, and mutes.",
    overwrites={hackathon.roles.BOARD: permissions.overwrites.READ_ONLY},
)
GATEWAY_LOGS = TextChannel(
    name="🚪gateway-logs🔑",
    topic="Joins and leaves.",
    overwrites={hackathon.roles.BOARD: permissions.overwrites.READ_ONLY},
)
MEMBER_LOGS = TextChannel(
    name="👥member-logs📋",
    topic="Nickname and role changes.",
    overwrites={hackathon.roles.BOARD: permissions.overwrites.READ_ONLY},
)
MESSAGE_LOGS = TextChannel(
    name="💬message-logs📝",
    topic="Deleted and edited messages.",
    overwrites={hackathon.roles.BOARD: permissions.overwrites.READ_ONLY},
)

CHANNELS = [
    WELCOME,
    RULES,
    TextChannel(
        name="🗣introductions✨",
        topic="Introduce yourself! Share your name, major, year, and hobbies/interests!",
        overwrites={roles.EVERYONE: permissions.overwrites.READ_WRITE},
    ),
    ChannelCategory(
        name="🗞 Spark Hub 📰",
        channels=[
            TextChannel(
                name="🚨fire🔥",
                topic="Never mute this one. Seriously.",
            ),
            TextChannel(name="💬board-chat🧠", topic="Safe space for board."),
            TextChannel(
                name="🧑‍🏫mentor-chat💡",
                topic="Safe space for mentors.",
                overwrites={hackathon.roles.MENTOR: permissions.overwrites.VIEW},
            ),
        ],
    ),
    ChannelCategory(
        name="📢 Info Hub 📚",
        channels=[
            TextChannel(
                name="📢announcements🚨",
                topic="The source of truth.",
            ),
            TextChannel(
                name="📚resources🤓",
                topic="Helpful links, docs, and tools for your hack.",
            ),
        ],
        overwrites={
            roles.EVERYONE: permissions.overwrites.READ_ONLY,
            hackathon.roles.BOARD: permissions.overwrites.READ_WRITE,
        },
    ),
    ChannelCategory(
        name="🗞 Hackers Hub 👨‍💻",
        channels=[
            TextChannel(name="💬general💼", topic="The chatting spot."),
            TextChannel(
                name="💬yapping🗣️", topic="Off-topic chatter. No hack talk here."
            ),
            TextChannel(name="😂memes🗿", topic="The culture."),
            TextChannel(
                name="💼linkedin🔗",
                topic="Share your LinkedIn and connect with fellow hackers!",
            ),
            TextChannel(
                name="📷photo-dump🎞️", topic="Drop your SparkHacks photos here!"
            ),
        ],
        overwrites={
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.SPONSOR: permissions.overwrites.VIEW,
            hackathon.roles.JUDGE: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="🛠️ Support Hub 🆘",
        channels=[
            ForumChannel(
                name="🤝looking-for-a-team🔍",
                post_guidelines="Looking for teammates or a team to join? Post your skills, your idea, and what you need.",
                tags=[
                    discord.ForumTag(name="Looking for Team", emoji="🔍"),
                    discord.ForumTag(name="Looking for Members", emoji="📢"),
                ],
                require_tag=True,
                default_reaction="🤝",
            ),
            ForumChannel(
                name="❓ask-sparkhacks📣",
                post_guidelines="Have a question about SparkHacks? Our organizers will answer!",
                tags=[
                    discord.ForumTag(name="Logistics", emoji="📦"),
                    discord.ForumTag(name="Rules", emoji="📜"),
                    discord.ForumTag(name="Events", emoji="🎉"),
                    discord.ForumTag(name="Other", emoji="📌"),
                ],
                require_tag=True,
                default_reaction="❓",
            ),
            ForumChannel(
                name="🧑‍🏫ask-a-mentor💬",
                post_guidelines="Stuck on something? Our mentors are here to help!",
                tags=[
                    discord.ForumTag(name="Ideation", emoji="💡"),
                    discord.ForumTag(name="Design", emoji="🎨"),
                    discord.ForumTag(name="Technical", emoji="⚙️"),
                    discord.ForumTag(name="Career", emoji="🚀"),
                ],
                require_tag=True,
                default_reaction="💡",
            ),
        ],
        overwrites={
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="🎤 Voice Chats 🎧",
        channels=[
            VoiceChannel(name="🛋️spark-lounge💬"),
            VoiceChannel(name="🧑‍🏫mentor-oh-1🎙️"),
            VoiceChannel(name="🧑‍🏫mentor-oh-2🎙️"),
            VoiceChannel(name="🧑‍🏫mentor-oh-3🎙️"),
        ],
        overwrites={
            hackathon.roles.HACKER: permissions.overwrites.VIEW,
            hackathon.roles.MENTOR: permissions.overwrites.VIEW,
        },
    ),
    ChannelCategory(
        name="🤖 Bots Hub ⚙️",
        channels=[
            TextChannel(name="💬commands🛠️", topic="Bother the bot here."),
            SYS_LOGS,
            MOD_LOGS,
            GATEWAY_LOGS,
            MEMBER_LOGS,
            MESSAGE_LOGS,
        ],
    ),
]
