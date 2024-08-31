import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import BOT_TOKEN as token
from button import menyu


bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu Aleykum botimizga Xush kelibsiz ", reply_markup=menyu)



@dp.message(F.text=='HFW 4.91')
async def Playstation(message:Message):
  await message.answer(text='https://www.pspx.ru/forum/showthread.php?t=114619')    


@dp.message(F.text=='HFW 4.90')
async def Playstation(message:Message):
  await message.answer(text='https://psx-core.ru/news/ps3_cfw_4_90_evilnat_39_s_cobra_v8_40/2023-03-08-1758')

@dp.message(F.text=='HFW 4.89')
async def Playstation(message:Message):
  await message.answer(text='https://www.pspx.ru/forum/showthread.php?t=112851')

@dp.message(F.text=='HFW 4.88')
async def Playstation(message:Message):
  await message.answer(text='https://www.pspx.ru/forum/showthread.php?t=111693')

@dp.message(F.text=='HFW 4.87' )
async def Playstation(message:Message):
  await message.answer(text='https://www.pspx.ru/forum/showthread.php?t=110940')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")