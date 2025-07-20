import discord
from dataclasses import dataclass

@dataclass
class Channel:
    name: str
    type: str

@dataclass
class Category:
    name: str
    channel: discord.CategoryChannel | None
    channels: list[Channel]

@dataclass
class Role:
    name: str
    color: str