from bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from random import randint
import time
import game_candy


class User_step(StatesGroup):
    take_candy = State()


@dp.message_handler(commands=['start']) # декоратор, обертка, изменяет поведение функции, но не меняет саму функцию.
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, привет мой хороший!')

@dp.message_handler(commands=['candy_game'], state=None)
async def start_game(message: types.Message):
    game_candy.new_game()
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, ну что-же, начнём игру...')
    time.sleep(1)
    await bot.send_message(message.from_user.id, text=f'Правила игры. На столе лежит 150 конфет. Побеждает тот, кто забрал последние конфеты.'
                                                      f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
    time.sleep(7)
    await bot.send_message(message.from_user.id, text=f'Определяем, кто ходит первый...')

    if game_candy.check_game():
        flag = randint(0, 2)
        if flag:
            time.sleep(2)
            await player_step(message)
        else:
            time.sleep(2)
            await bot_take(message)

async def player_step(message):
    time.sleep(2)
    await message.answer(text=f'{message.from_user.first_name}, твой ход, сколько возьмёшь конфет?')
    await User_step.take_candy.set()

@dp.message_handler(state=User_step.take_candy)
async def take_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['take_candy'] = message.text
    take = data['take_candy']
    if game_candy.check_game():
        if take.isdigit():
            take = int(take)
            if 0 < take < 29 and take <= game_candy.get_total():
                game_candy.take_candy(take)
                if await winner(message, take, 'player'):
                    return
                time.sleep(2)
                await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} взял {take} конфет,'
                                                                f'на столе осталось {game_candy.get_total()} штук')
                await state.finish()
                await bot_take(message)
            else:
                time.sleep(1)
                await bot.send_message(message.from_user.id, text='Нарушаешь правила игры! Нужно от 1 до 28 штук')
        else:
            time.sleep(1)
            await bot.send_message(message.from_user.id, text='Некорректный ввод, попробуй еще раз.')

async def bot_take(message):
    time.sleep(2)
    await bot.send_message(message.from_user.id, text=f'Ходит Бот')
    total = game_candy.get_total()
    if total < 29:
        bot_step = total
    else:
        division = total // 28
        bot_step = total - ((division * game_candy.get_max_take()) + 1)
        if bot_step == -1:
            bot_step = game_candy.get_max_take() - 1
        if bot_step == 0:
            bot_step = game_candy.get_max_take()
    while bot_step > 28 or bot_step < 1:
        bot_step = randint(1, 28)
    game_candy.take_candy(bot_step)
    time.sleep(2)
    await bot.send_message(message.from_user.id, text=f'Бот взял {bot_step} конфет, на столе {game_candy.get_total()} конфет.')
    if await winner(message, bot_step, 'Бот'):
        return
    await player_step(message)

async def winner(message, take: int, player: str):
    if game_candy.get_total() <= 0:
        if player == 'player':
            time.sleep(2)
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} взял {take} конфет и '
                                                              f'одержал победу!!!!\nБот отдай все конфеты победителю!')
            time.sleep(2)
            await bot.send_message(message.from_user.id, text=f'Игра окончена...  Молодец, возвращайся, если захочешь сыграть')
        else:
            time.sleep(2)
            await bot.send_message(message.from_user.id, text=f'Бот взял {take} конфет и '
                                                              f'одержал победу!!!!\n{message.from_user.first_name} позоришь ты нас...')
            time.sleep(2)
            await bot.send_message(message.from_user.id, text=f'Игра окончена... навсегда...   для тебя {message.from_user.first_name}\n'
                                                              f'ахахаха)))))')
        game_candy.new_game()
        return True
    else:
        return False


@dp.message_handler(commands=['tic_tac_toe'], state=None)
async def start_game(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, извини, но игра еще в разработке...')


@dp.message_handler(commands=['weather'], state=None)
async def start_game(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, о погоде пока не узнать....\n'
                                                      f'Разработчик не успевает...')

