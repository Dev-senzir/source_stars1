import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from YukkiMusic import app


@app.on_message(filters.command(['مهنتي'], prefixes=""))
def get_user_info(_, message):
    url = f"https://t.me/{message.from_user.username}"
    age = random.randint(20, 30)
    jobs = ["مهندس", "دكتور", "مدرس", "حرامي"]
    job = random.choice(jobs)
    statuses = ["متزوج", "سنجل", "مطلق", "ارمل"]
    status = random.choice(statuses)
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"اسمك هو: {message.from_user.first_name}", url=url)],
            [InlineKeyboardButton(f"سنك هو: {age}", callback_data=f"age_{age}")],
            [InlineKeyboardButton(f"مهنتك هي: {job}", callback_data=f"job_{job}")],
            [InlineKeyboardButton(f"حالتك الإجتماعيه هي: {status}", callback_data=f"status_{status}")]
        ]
    )
    app.send_photo(
        chat_id=message.chat.id,
        photo=url,
        reply_markup=inline_keyboard,
        reply_to_message_id=message.message_id
    )

