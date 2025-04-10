from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command

BOT_TOKEN = '7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def command_start(message: Message):
    await message.answer('Здравствуйте, вас приветствует эхо бот')

async def command_help(message: Message):
    await message.answer('Здравствуйте, чем могу помочь вам')

async def send_photo(message: Message):
    await message.answer_photo(message.photo[0].file_id)

async def send_video(message: Message):
    await message.reply_video(message.video.file_id)

async def send_audio(message: Message):
    await message.reply_audio(message.audio.file_id)

async def send_file(message: Message):
    await message.reply_document(message.document.file_id)

async def echo_comm(message: Message):
    await message.reply(text = message.text)

dp.message.register(command_start, Command(commands='start'))
dp.message.register(command_start, Command(commands='help'))
dp.message.register(send_photo, F.photo)
dp.message.register(send_video, F.video)
dp.message.register(send_audio, F.audio)
dp.message.register(send_file, F.document)
dp.message.register(echo_comm)


if __name__ == '__main__':
    dp.run_polling(bot)


# https://api.telegram.org/bot7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI/getUpdates
# https://api.telegram.org/bot7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI/send_photo

