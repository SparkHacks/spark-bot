import discord
from dataclasses import dataclass

@dataclass
class Channel:
    name: str
    type: str

@dataclass
class Role:
    name: str
    permissions: discord.Permissions = discord.Permissions.none()
    color: discord.Color = discord.Color.random()
    hoist: bool = False

@dataclass
class Category:
    name: str
    channels: list[Channel]
    roles: list[Role]
    channel: discord.CategoryChannel = None

@dataclass
class Team:
    name: str
    members: list[str]