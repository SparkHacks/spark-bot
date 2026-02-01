import discord

rules = discord.Embed(
    description="Welcome! Please read and follow these rules to keep the hackathon inclusive, productive, and fun for everyone.\n",
    color=discord.Color(int("#A5A8C3"[1:], 16)),
)

rules.add_field(
    name="🧠 Rule 1 — Be Respectful 🤝",
    value=(
        "Be kind and treat everyone with respect.\n\n"
        "**Zero tolerance for:** harassment, discrimination, hate speech, racism, sexism, homophobia, transphobia, ableism, slurs, impersonation, or sharing personal information without consent."
    ),
    inline=False,
)

rules.add_field(
    name="🚫 Rule 2 — No NSFW/NSFL Content 🔞",
    value=(
        "NSFW or NSFL content is **not allowed**.\n\n"
        "**Includes:** messages, images, links, usernames, nicknames, and profile pictures."
    ),
    inline=False,
)

rules.add_field(
    name="📢 Rule 3 — No Spam 🚯",
    value=(
        "Spam of any kind is not tolerated.\n\n"
        "**Includes:** mass pings, flooding, emote spam, or using @everyone/@here.\n\n"
        "**Do not spam or DM mentors, judges, or board.**"
    ),
    inline=False,
)

rules.add_field(
    name="🧾 Additional Guidelines 📌",
    value=(
        "These rules are not exhaustive and may be updated at any time. If board member asks you to stop doing something, please comply.\n\n"
        "In addition, this Discord server follows:\n"
        "• [Discord Terms of Service](https://discord.com/terms) and [Community Guidelines](https://discord.com/guidelines)\n"
        "• [UIC Department of Computer Science Student Code of Conduct](https://www.cs.uic.edu/~grad/CS_Code_of_Conduct.pdf)\n"
        "• [SparkHacks Code of Conduct](https://outgoing-bubble-324.notion.site/Code-of-Conduct-2bdb7981cdc3815ba451eca455220dcd)"
    ),
    inline=False,
)

rules.add_field(
    name="✅🎉 Verification & Access 🎉",
    value=(
        "To gain full access to the server:\n"
        "1️⃣ **Read** all rules and guidelines above\n"
        "2️⃣ **Acknowledge and agree** to follow them\n"
        "3️⃣ **React** with ✅ under this message to gain access\n\n"
        "By reacting, you confirm that you understand and agree to follow all server rules."
    ),
    inline=False,
)

rules.set_author(name="SparkHacks Rules", icon_url="attachment://icon.png")
rules.set_thumbnail(url="attachment://icon.png")
