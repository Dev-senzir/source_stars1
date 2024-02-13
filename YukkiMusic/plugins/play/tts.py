import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from YukkiMusic import app
from config import OWNER_ID
from YukkiMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic.misc import SUDOERS

@app.on_message(command(["اوامر الميوزك","الاوامر"]))
async def abrag(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر المجموعه", callback_data="zein " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر القنوات", callback_data="tomm " + str(m.from_user.id))],
        [InlineKeyboardButton("اوامر اضافيه", callback_data="manoo " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر البوت", callback_data="jokk " + str(m.from_user.id))],
        [InlineKeyboardButton("اوامر الادمن", callback_data="lenda " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر المطور", callback_data="motwr " + str(m.from_user.id))],
        [InlineKeyboardButton("اوامر التسليه", callback_data="tslya " + str(m.from_user.id))] +
        [InlineKeyboardButton("مميزات السورس", callback_data="mooms " + str(m.from_user.id))],

    ])
    await m.reply_text("• مرحبآ بك عزيزي × قسم ( الاوامر ) آنقر علي الازرار لآختيار الامر - 💠\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^zein (\\d+)$"))
async def elgadee(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
◍ - اوامر تشغيل البوت في المجموعات - √

◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به  •
◍ -『 **فيديو** 』\n ثم اسم مقطع الفيديو او الرابط الخاص به  •
◍ -『 **تنزيل** 』\n ثم اسم المقطع المراد تنزيله من موقع اليوتيوب مباشر او الرابط الخاص به  •
◍ -『 **ريلود** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^tomm (\\d+)$"))
async def eldaloo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
◍ - **جزء القنوات** - √
◍ - اوامر تشغيل البوت في القنوات 👇 - √

◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به لتشغيله بقناتك  •
◍ -『 **فيديو** 』\nثم اسم الفيديو او الرابط الخاص به لتشغيله بقناتك  •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ.

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^manoo (\\d+)$"))
async def elhout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
✅ | - إليك قسم ( الاوامر الاضافيه ) للبوت  •
✅ | - جميع الاوامر تعمل بدون علامات  •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

◍ -『 **حدد** 』\n ثم رقم المجموعات الذي تستخدم بوتك فيديو بنفس الوقت •

◍ -『 **وضع شغل** 』\n لضبط وضع تحكم التشغيل للأدمن او للاعضاء داخل مجموعتك  •

◍ -『 **القائمه** 』\n لعرض قائمه التشغيل الخاصه بك  •

◍ -『 **حذف القائمه** 』\n لحذف قائمه التشغيل الخاصه بك  •

◍ -『 **لغه** 』\n لتغيير لغة البوت إلي اي لغه اخري  •

◍ -『 **احصائيات** 』\n لعرض قسم الاحصائيات العامه للبوت ولترند التشغيل العالمي •

◍ -『 **ريلود** 』\n لتحديث قائمة المشرفين داخل مجموعتك •

◍ -『 **بينج** 』\n لقياس سرعه التشغيل علي السيرفر وعرض تفاصيل معلومات التشغيل •

◍ -『 **كلمات** 』\n ثم اسم الاغنيه لجلب كلمات الاغنيه كامله بصيغه النصوص •

◍ -『 **تنزيل** 』\n ثم اسم المقطع او الرابط الخاص به لتحميله مباشر من اليوتيوب •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^jokk (\\d+)$"))
async def elhamal(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

✅<u>**اوامر البوت:**</u>

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
✅ | - إليك قسم ( الاوامر الاضافيه ) للبوت  •
✅ | - جميع الاوامر تعمل بدون علامات  •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

◍ -『 **حدد** 』\n ثم رقم المجموعات الذي تستخدم بوتك فيديو بنفس الوقت •

◍ -『 **وضع شغل** 』\n لضبط وضع تحكم التشغيل للأدمن او للاعضاء داخل مجموعتك  •

◍ -『 **القائمه** 』\n لعرض قائمه التشغيل الخاصه بك  •

◍ -『 **حذف القائمه** 』\n لحذف قائمه التشغيل الخاصه بك  •

◍ -『 **لغه** 』\n لتغيير لغة البوت إلي اي لغه اخري  •

◍ -『 **احصائيات** 』\n لعرض قسم الاحصائيات العامه للبوت ولترند التشغيل العالمي •

◍ -『 **ريلود** 』\n لتحديث قائمة المشرفين داخل مجموعتك •

◍ -『 **بينج** 』\n لقياس سرعه التشغيل علي السيرفر وعرض تفاصيل معلومات التشغيل •

◍ -『 **كلمات** 』\n ثم اسم الاغنيه لجلب كلمات الاغنيه كامله بصيغه النصوص •

◍ -『 **تنزيل** 』\n ثم اسم المقطع او الرابط الخاص به لتحميله مباشر من اليوتيوب •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^lenda (\\d+)$"))
async def elthawr(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
🎧 | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل المجموعات )  •
🔻 | - الاوامر تعمل بدون استخدام اي علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬

◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •
◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •
◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •
◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
🎙️ | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل القنوات )  •
🔻 | - الاوامر تعمل بدون استخدام اي علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬

◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •
◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •
◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •
◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬."""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^motwr (\\d+)$"))
async def eldaloo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

• | رفع ثانوي لرفع الشخص مطور ثانوي .🕷

• | رفع ادمن لرفع الشخص ادمن .🕷

• | تنزيل ثانوي الشخص من المطورين الثانويين .🕷

• | تنزيل ادمن الشخص من الادمنيه .🕷

• | الادمنيه لعرض ادمنيه البوت .🕷

• | الثانويين لعرض المطورين الثانويين .🕷

• | اذاعه لعمل اذاعه ف البوت .🕷
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ.

╚━━━※᥉᥆ᥙᖇᥴᥱ ᖇᥱƒᤁ※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)
    
    
@app.on_callback_query(filters.regex("^mooms (\\d+)$"))
async def eldaloo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

⚡↰ قول↳✧
🌧️↰ بايو  ↳✧
⚡☔↰ سورس ↳✧
🌖↰ احكام ↳✧
🌗↰ نكته ↳✧
🌠↰ ايدي ↳✧
🪐↰ صوره ↳✧
🌄↰ انمي ↳✧
🦓↰ متحركه ↳✧
🦕↰ سوره ↳✧
🦢↰ الشيخ ↳✧
🦠↰ استوري ↳✧
🍒↰ الرابط ↳✧
🧊↰ غنيلي ↳✧
🍯↰ افتار عيال  ↳✧
🥮↰ افتارات مكس ↳✧
🍪↰ اقتباسات ↳✧
🍧↰ هيدرات ↳✧
🥧↰ نداء ↳✧
🚲↰ زوجني ↳✧
🎪↰ ابراج ↳✧
🏭↰ احرف ↳✧
🗻↰ انصحني ↳✧
🔓↰ اذكار ↳✧
⚱️↰ لو خيروك ↳✧
🔩↰ كتبات ↳✧
🗃️↰ صراحه ↳✧
🪝↰ زخرفه ↳✧
🦺↰ مين في الكول ↳✧
👕↰ المالك ↳✧
🪡↰ الالعاب ↳✧
🎰↰ معلوماته ↳✧
🎛️↰ افتارات بنات ↳✧
🧵↰ افتارات عيال ↳✧
🎻↰ كت بالصوره ↳✧

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)    
    
    
@app.on_callback_query(filters.regex("^tslya (\\d+)$"))
async def elgadee(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦  ※━━━╗

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
◍ - اوامر تشغيل البوت في المجموعات - √

◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به  •
◍ -『 **فيديو** 』\n ثم اسم مقطع الفيديو او الرابط الخاص به  •
◍ -『 **تنزيل** 』\n ثم اسم المقطع المراد تنزيله من موقع اليوتيوب مباشر او الرابط الخاص به  •
◍ -『 **ريلود** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

╚━━━※𝗦َِ𝗢َِ𝗨َِ𝗥َِ𝗖َِ𝗘 𝗦ََِ𝗧َِ𝗔َِ𝗥َِ𝗦※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)    