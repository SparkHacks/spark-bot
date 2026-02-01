from dataclasses import dataclass, field
from typing import Union

import discord


@dataclass(frozen=True)
class Role:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    color: Union[discord.Color, str] = "#FFFFFF"
    hoist: bool = False

    def __post_init__(self):
        if isinstance(self.color, str):
            object.__setattr__(
                self, "color", discord.Color(int(self.color[1:], 16))
            )


@dataclass(frozen=True)
class RoleCategory:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    color: discord.Color = discord.Color(int("292B2F", 16))
    hoist: bool = False

    def __post_init__(self):
        object.__setattr__(
            self,
            "name",
            f"\u2063{self.name:{'\u2002'}^{34}}{'\u2002' * 5}\u2063",
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
class ChannelCategory:
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
