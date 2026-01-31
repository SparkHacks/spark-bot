from configs.teams import (
    COMMUNICATIONS,
    DIRECTORS,
    EXPERIENCE,
    LEADS,
    LOGISTICS,
    OUTREACH,
    WEBDEV,
)
from utils.dataclasses import Team

TEAMS = [
    Team(name="Director", members=DIRECTORS),
    Team(name="Lead", members=LEADS),
    Team(name="Communications", members=COMMUNICATIONS),
    Team(name="Experience", members=EXPERIENCE),
    Team(name="Logistics", members=LOGISTICS),
    Team(name="Outreach", members=OUTREACH),
    Team(name="Webdev", members=WEBDEV),
]
