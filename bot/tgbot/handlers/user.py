from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import datetime
import asyncio
from aiogram import Bot
from tgbot.config import load_config

from tgbot.models.json_event import get_events_data
from tgbot.models.json_event import converter

user_router = Router()

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode="HTML")


@user_router.message(CommandStart())
async def user_start(message: Message):
    events = converter()
    info = get_events_data()
    info = list(info.values())
    print(info)
    while True:
        if str(datetime.datetime.now().strftime("%d.%m.%Y")) in events:
            await bot.send_photo(message.chat.id, info[0]["image_src"], caption=f'*{info[0]["title"]}*\nГде: *{info[0]["location"]}*\n*{info[0]["date"]}*\n{info[0]["cost"]}\nРегистрация по ссылке:\n{info[0]["link"]}', parse_mode="Markdown")
            await asyncio.sleep(86400)
        else:
            await message.answer("Сегодня нет мероприятий")
            await asyncio.sleep(86400)
