import random
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message 
from aiogram.filters import Command

BOT_TOKEN = '7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5
users = {}


def random_digit() -> int:
    return random.randint(1,100)

@dp.message(Command(commands=['start']))
async def command_start(message: Message):
    await message.answer('Приветствую тебя\n'
                        'Ты зашел в игру "Угадай число"\n'
                        'Чтобы прочесть правила - напиши "/help"')
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in game': False,
            'Attemts': None,
            'Total_games': 0,
            'Secret_Number': None,
            'Wins': 0}
    
@dp.message(Command(commands=['help']))
async def command_help(message: Message):
    await message.answer('Правила игры\n\n'
                        'Ты должен угадать число от 1 до 100\n'
                        'Ты можешь остановить игру, введя команду /cancel\n'
                        'Ты можешь посмотреть статистику игры, введя команду /stat\n'
                        'У тебя всего 5 попыток. Готов начать?')

@dp.message(Command(commands=['cancel']))
async def command_cancel(message: Message):
    if users[message.from_user.id]['in game'] == True:
        users[message.from_user.id]['in game'] = False
        await message.answer('Вы остановили игру, начнем '
                             'еще раз?')
    elif users[message.from_user.id]['in game'] == False:
        await message.answer('Вы еще не начали игру :)')

@dp.message(Command(commands=['stat']))
async def command_stat(message: Message):
    if users[message.from_user.id]['in game'] == False:
        await message.answer(f'Вот ваша статистика:\n\n '
                             f'Игр сыграно {users[message.from_user.id]["Total_games"]}\n '
                             f'Количество выигрышей {users[message.from_user.id]["Wins"]}')
    elif users[message.from_user.id]['in game'] == True:
        await message.answer('Смотреть статистику можно только '
                         'вне игры!')
    
@dp.message(F.text.lower().in_(['да','давай','начать игру']))
async def positive_answer(message: Message):
    if users[message.from_user.id]['in game'] == False:
        users[message.from_user.id]['in game'] = True
        users[message.from_user.id]['Attemts'] = ATTEMPTS
        users[message.from_user.id]['Secret_Number'] = random_digit()
        await message.answer('Я загадал число - отгадывай')
    elif users[message.from_user.id]['in game'] == True:
        await message.answer('Ты уже в игре - отгадывай числа :)')

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def check_digit(message: Message):
    if users[message.from_user.id]['in game'] == True:
        if int(message.text) == users[message.from_user.id]['Secret_Number']:
            users[message.from_user.id]['in game'] = False
            users[message.from_user.id]['Total_games'] += 1 
            users[message.from_user.id]['Wins'] += 1 
            await message.answer('Вы победили!\n\n'
                                 'Можете посмотреть статистику "/stat"')
        elif int(message.text) != users[message.from_user.id]['Secret_Number']:
            if int(message.text) > users[message.from_user.id]['Secret_Number']:
                users[message.from_user.id]['Attemts'] -= 1
                await message.answer('Загаданное мной число меньше\n'
                                    f'Осталось {users[message.from_user.id]["Attemts"]} попытки(ок)')
            elif int(message.text) < users[message.from_user.id]['Secret_Number']:
                users[message.from_user.id]['Attemts'] -= 1
                await message.answer('Загаданное мной число больше\n'
                                    f'Осталось {users[message.from_user.id]["Attemts"]} попытки(ок)')
    else:
        await message.answer('Сначала нужно начать игру!'
                             'Напиши в чат "Начать игру"')
    if users[message.from_user.id]['in game'] == True and users[message.from_user.id]['Attemts'] == 0:
        users[message.from_user.id]['in game'] = False
        users[message.from_user.id]['Total_games'] += 1 
        await message.answer('Вы проиграли!\n\n'
                                 f'Загаданное мной число было {users[message.from_user.id]['Secret_Number']}\n'
                                 'Можете посмотреть статистику "/stat"')
    
@dp.message()
async def another_sms(message: Message):
    await message.answer('Мой функционал довольно ограничен, '
                         'поэтому будьте добры не загружать меня '
                         'лишними смс :)')
    

if __name__ == '__main__':
    dp.run_polling(bot)












# https://api.telegram.org/bot7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI/getUpdates
# https://api.telegram.org/bot7880667747:AAHM4AJOEO2V4TusSJqDFWHMnmlBpydG7JI/send_photo

