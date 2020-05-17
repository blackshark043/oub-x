#this module originally created by @spechide https://github.com/SpEcHiDe/UniBorg
#ported to oub by @heyworld

import asyncio
from telethon import events
from telethon.tl import functions, types
from userbot.events import register
from userbot import BOTLOG, BOTLOG_CHATID, LOGS


NO_PM_LOG_USERS = []


@register(incoming=True, disable_edited=True)
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if event.is_private and not (await event.get_sender()).bot:
        chat = await event.get_chat()
        if chat.id not in NO_PM_LOG_USERS and chat.id:
            try:
                e = await event.client.get_entity(int(BOTLOG_CHATID))
                fwd_message = await event.client.forward_messages(
                    e,
                    event.message,
                    silent=True
                )
            except Exception as e:
                LOGS.warn(str(e))
