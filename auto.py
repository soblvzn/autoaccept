from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton as ib
from logging import basicConfig

basicConfig()

bot = Bot(token="", parse_mode="HTML")
dp = Dispatcher(bot)
txt = """<b>by soblazncc?</b>"""
ph = "https://telegra.ph//file/12f2577ffc46b9f08f9e5.jpg"
markup = InlineKeyboardMarkup()
markup.row(ib("🛍 developer", url="https://t.me/soblazncc"))

@dp.chat_join_request_handler()
async def join(request: ChatJoinRequest):
    await request.approve()
    await bot.send_photo(request.from_user.id, ph, caption=txt, reply_markup=markup)

@dp.message_handler(commands="start")
async def start(m: Message):
	await m.answer(f"Привет, {m.from_user.get_mention()}")

if __name__ == "__main__":
	executor.start_polling(dp)