#предварительно инсталлим: pip install aiogram.py
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='токен сюды @bot_father')
disp = Dispatcher(bot)

@disp.message_handler()
async def main(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(disp)
