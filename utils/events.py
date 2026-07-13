from datetime import timedelta

import discord


async def get_audit_log_entry(
    guild: discord.Guild, action: discord.AuditLogAction, target_id: int
) -> discord.AuditLogEntry | None:
    return await guild.audit_logs(action=action, limit=5).find(
        lambda entry: entry.target.id == target_id
        and entry.created_at > discord.utils.utcnow() - timedelta(seconds=5)
    )
