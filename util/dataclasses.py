from dataclasses import dataclass, field

import discord

from static import colors


@dataclass(frozen=True)
class Role:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    color: discord.Color = discord.Color.default()
    hoist: bool = False
    mentionable: bool = False


@dataclass(frozen=True)
class RoleCategory:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    color: discord.Color = colors.CATEGORIES
    hoist: bool = False
    mentionable: bool = False

    def __post_init__(self):
        object.__setattr__(
            self,
            "name",
            f"\u2063{self.name:{'\u2002'}^{34}}{'\u2002' * 5}\u2063",
        )


@dataclass(frozen=True)
class TextChannel:
    name: str
    topic: str | None = None
    overwrites: dict[Role, discord.PermissionOverwrite] = field(default_factory=dict)


@dataclass(frozen=True)
class VoiceChannel:
    name: str
    overwrites: dict[Role, discord.PermissionOverwrite] = field(default_factory=dict)


@dataclass(frozen=True)
class ForumChannel:
    name: str
    post_guidelines: str | None = None
    tags: list[discord.ForumTag] = field(default_factory=list)
    require_tag: bool = False
    default_reaction: str | None = None
    overwrites: dict[Role, discord.PermissionOverwrite] = field(default_factory=dict)


@dataclass(frozen=True)
class ChannelCategory:
    name: str
    channels: list[TextChannel | VoiceChannel | ForumChannel]
    overwrites: dict[Role, discord.PermissionOverwrite] = field(default_factory=dict)
