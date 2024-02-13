import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from asyncio import gather






@app.on_message(command(["معلوماته", "كشف"]) & filters.group & ~filters.edited) 
async def hshs(client: Client, message: Message):      
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name#
    user_id = message.reply_to_message.from_user.id#
    chat_idd = message.chat.id#
    chat_username = f"@{message.chat.username}" #
    chat_name = message.chat.title#
    username = f"@{message.reply_to_message.from_user.username}"#
    async for photo in client.iter_profile_photos(message.reply_to_message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**[𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦˼⁩](https://t.me/Y_H_E)\n\n🐉 ¦ ꪀᥲ️ꪔᥱ : {name}\n🤡 ¦ ᴜѕᴇ : {username}\n🔥 ¦ Ꭵَժ : `{user_id}`\n🗿 ¦ Ꭵժ ᥴ𝗁ᥲ️ƚ : `{chat_idd}`\n🐰 ¦ 𝚌𝚑𝚊𝚝 : {chat_name}\n🐊 ¦ ᘜᖇ᥆υρ : {chat_username} \n**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        ),
    )     


