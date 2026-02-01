from dataclasses import dataclass, field

import discord


@dataclass(frozen=True)
class Role:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    hex_color: str = "#FFFFFF"
    color: discord.Color = field(init=False)
    hoist: bool = False

    def __post_init__(self):
        object.__setattr__(
            self, "color", discord.Color(int(self.hex_color[1:], 16))
        )


@dataclass(frozen=True)
class Channel:
    name: str
    type: str = "text"
    roles: list[Role] = field(default_factory=list)
    overwrites: dict[Role, discord.PermissionOverwrite] = field(
        default_factory=dict
    )


@dataclass(frozen=True)
class Category:
    name: str
    channels: list[Channel]
    roles: list[Role] = field(default_factory=list)
    overwrites: dict[Role, discord.PermissionOverwrite] = field(
        default_factory=dict
    )


@dataclass(frozen=True)
class Team:
    name: str
    members: list[str]
