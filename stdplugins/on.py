""".on Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("on"))
async def _(event):
    if event.fwd_from:
        return
    mentions =       "`i am ON My Mastor \n\nTelethon version: 1.10.10 \n\nPython: 3.8.3 \n--------------------------- \nUser: is the one who is using it \n\nDatabase Status: Basiclly Telegram Databases functioning is normal! just sometimes it creates hoax!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
