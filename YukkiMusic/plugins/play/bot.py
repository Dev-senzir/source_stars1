#✘ ITALY MUSIC @I6ALY ✘
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from YukkiMusic import app


@app.on_message(filters.command(['بوت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 6275274612:
             rank = "**يالهوي ده مالك السورس بنفسو ياعيال في البار😱⚡️**"
        elif member.status == 'creator':
             rank = "**مـالك الـبـار 🫡⚡️**"
        elif member.status == 'administrator':
             rank = "**مـشـرف الـبـار🫡⚡️**"
        else:
             rank = "**لاسف انت عضو فقير🥺💔**"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    async for photo in client.iter_profile_photos("me", limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**نعم حبيبي :** {italy} 🥰❤\n**انا اسمي القميل :** {bot_name} 🥺🙈\n**رتبتك هي :** {rank}""", reply_markup=keyboard)

#✘ ITALY MUSIC @I6ALY ✘

