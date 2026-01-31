from utils import env_int_list

DIRECTORS = env_int_list("DIRECTORS")
LEADS = env_int_list("LEADS")

COMMUNICATIONS = env_int_list("COMMUNICATIONS")
EXPERIENCE = env_int_list("EXPERIENCE")
LOGISTICS = env_int_list("LOGISTICS")
OUTREACH = env_int_list("OUTREACH")
WEBDEV = env_int_list("WEBDEV")

BOARD = DIRECTORS + COMMUNICATIONS + EXPERIENCE + LOGISTICS + OUTREACH + WEBDEV
