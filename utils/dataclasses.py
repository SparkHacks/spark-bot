from dataclasses import dataclass, field

import discord


@dataclass
class Role:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    hex_color: str = "#FFFFFF"
    color: discord.Color = field(init=False)
    hoist: bool = False

    def __post_init__(self):
        self.color = discord.Color(int(self.hex_color[1:], 16))


@dataclass
class Channel:
    name: str
    type: str = "text"
    roles: list[Role] = field(default_factory=list)


@dataclass
class Category:
    name: str
    channels: list[Channel]
    channel: discord.CategoryChannel = None
    roles: list[Role] = field(default_factory=list)


@dataclass
class Team:
    name: str
    members: list[str]
