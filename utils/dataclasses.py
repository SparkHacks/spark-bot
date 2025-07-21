import discord
from dataclasses import dataclass

@dataclass
class Channel:
    name: str
    type: str

@dataclass
class Category:
    name: str
    channels: list[Channel]
    channel: discord.CategoryChannel = None

@dataclass
class Role:
    name: str
    permissions: discord.Permissions = None
    color: discord.Color = discord.Color.random()

@dataclass
class Team:
    name: str
    members: list[str]