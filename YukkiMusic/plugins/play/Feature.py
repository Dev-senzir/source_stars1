

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
    command(["البنك","بنك النجوم"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم لعبة بنك النجوم\n
⧛ ⋖≔𖣥≕✯𝗦𝗧𝗔𝗥𝗦✯≔𖣥≕⋗ ⧚

🏦 اوامر لعبه البنك ⇊

👮‍♂️ « المطور » ⇊
════════ ××× ════════ٴ
➕╖ اضف فلوس + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ حذف حسابه «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ حذف حساب + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ تصفير البنك «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
════════ ××× ════════ٴ
📑╖ انشاء «» فتح حساب بنكي
🤑╢ فلوسي «» اموالي
💸╢ فلوسه «» امواله ❬ بالرد علي الشخص ❭
🏦╢ بنكي «» حسابي
💰╢ بنكه «» حسابه ❬ بالرد علي الشخص ❭
♻️╢ تحويل + المبلغ
☠️╢ كنز
🤖╢ استثمار + المبلغ
🍃╢ حظ + المبلغ
⏫╢ مضاعفه «» مضاربه + المبلغ
🎯╢ عجله الحظ
🤞╢ رشوه
🥺╢ بقشيش
⏳╢ راتب
📎╢ سرقه «» اسرق ❬ بالرد علي الشخص ❭
🚔╢ شرطه «» شرطة ❬ بالرد علي الشخص ❭
⭐️╢ حمايه اموالي «» ❬ لحمايه اموالك من السرقه ❭
👮╢ شرطه + اليوزر
💂‍♀️╢ توب الحراميه «» توب السرقه
⤴️╜ توب الفلوس «» توب فلوس


⧛ ⋖≔𖣥≕✯𝗦𝗧𝗔𝗥𝗦✯≔𖣥≕⋗ ⧚""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗧𝗔𝗥𝗦 ⌝⚡", url=f"https://t.me/Y_H_E"),                        
                 ],[
                    InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
           ]
        ),
    )

