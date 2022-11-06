from aiogram import Dispatcher, types
from aiogram import Bot
from aiogram.utils import executor

bot=Bot(token="5671146593:AAFmKWrCU3CqmMebwwSrnq1c1-Kf_qsmOls")
dp= Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id=message.chat.id
    text="введи число от 1 до 5"

    
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())

    if get_message==1:
        print("привет")
    
executor.start_polling(dp)