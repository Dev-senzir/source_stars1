import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint


@app.on_message(
    command(["ساروت", "الساروت"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⧛ ⋖≔𖣥≕✯𝗦𝗧𝗔𝗥𝗦✯≔𖣥≕⋗ ⧚\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⧛ ⋖≔𖣥≕✯𝗦𝗧𝗔𝗥𝗦✯≔𖣥≕⋗ ⧚**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["ذكاء اصطناعي"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/b3a20ffde6f7e3be1fc2a.jpg",
        caption=f"""**⩹⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗧𝗔𝗥𝗦⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس النجوم\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ sᴏᴜʀᴄᴇ sᴇᴢᴀʀ ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𓆰هاشمي】ۦﭑﭑﻟﺴِٰﭑﭑࢪَِٰﯠَِٰتِٰۦٰ۪۫ۦٰﮧ۬⋆ۦ】", url=f"https://t.me/ALSAROT"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗧𝗔𝗥𝗦 ⌝⚡", url=f"https://t.me/Y_H_E"),
                ],

            ]

        ),

    )



    