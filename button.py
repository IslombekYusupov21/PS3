from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="HFW 4.91"), KeyboardButton(text="HFW 4.89")],
        [KeyboardButton(text="HFW 4.89"), KeyboardButton(text="HFW 4.89")],
        [KeyboardButton(text="HFW 4.89"), KeyboardButton(text="HFW 4.89")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

