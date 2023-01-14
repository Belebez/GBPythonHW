import random
from contextlib import suppress
from distutils.cmd import Command

from aiogram.dispatcher.filters import state
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
from bot_config import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from random import randint

import datetime
import requests
import time
import game_candy, game_ttt
from weather import open_weather_token

class User_step(StatesGroup):

    take_candy = State()
    weather_user = State()
    out_weather = State()
    game_ttt = State()
    start_user = State()


@dp.message_handler(commands=['greetings'], state=None) # декоратор, обертка, изменяет поведение функции, но не меняет саму функцию.
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, привет мой хороший!')


########################################################################################################################
########################################################################################################################
########################################################################################################################

# Раздел игры "Конфеты"
@dp.message_handler(commands=['candy_game'], state=None)
async def start_game(message: types.Message):
    game_candy.new_game()
    await User_step.take_candy.set()
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


########################################################################################################################
########################################################################################################################
########################################################################################################################

# Раздел игры Крестики-нолики

@dp.message_handler(commands=['tic_tac_toe'], state=None)
async def start_test(message: types.Message):
    await message.answer(text=f'Приветствую тебя мой друг.\n \nЧтобы начать игру нажми на --> /new_game')


user_data = {}
callback_numbers = CallbackData('btn','num')
symbol_x = '❌'
symbol_o = '⭕'
symbol_undef = '◻'
buttons = []


@dp.message_handler(commands=['new_game'])
async def new_game(message: types.Message):
    global buttons
    buttons = []
    await message.answer(text=f'Поехали! {message.from_user.first_name} твой ход.')
    time.sleep(1.5)
    await create_keyboard(message)


# создаём игровое поле
async def create_keyboard (message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(9):
        buttons.append(types.InlineKeyboardButton(text=symbol_undef, callback_data=callback_numbers.new(num=str(i))))
    keyboard.add(*buttons)
    restart_game = types.InlineKeyboardButton(text='Начать заново', callback_data='restart')
    keyboard.add(restart_game)
    await message.answer(f'Крестики-нолики\n', reply_markup=keyboard)

# изменяем клавиатуру после хода игрока
def new_keyboard(num):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    del buttons[num]
    buttons.insert(num, types.InlineKeyboardButton(text=symbol_x, callback_data=callback_numbers.new(num=str(num))))
    keyboard.add(*buttons)
    restart_game = types.InlineKeyboardButton(text='Начать заново', callback_data='restart')
    keyboard.add(restart_game)
    return keyboard

# получаем информацию о нажатой кнопке и в зависимости от игрового поля, отправляем на изменение
@dp.callback_query_handler(callback_numbers.filter(num=['0', '1', '2', '3', '4', '5', '6', '7', '8']))
async def play_player(call: types.CallbackQuery, callback_data: dict):
    num = int(callback_data['num'])
    if buttons[num]['text'] != symbol_x or buttons[num]['text'] != symbol_o:
        with suppress(MessageNotModified):
            await call.message.edit_reply_markup(reply_markup=new_keyboard(num))
            if await is_win(call, buttons, symbol_x):
                await call.answer(f'Ты выиграл \U0001F451, поздравляю!!! \U0000270A\U0001F680', show_alert=True)
                return
            if await is_draw(call, buttons):
                await call.answer(f'\U0001F642Ничья', show_alert=True)
                return
            await play_bot(call, callback_data)
    await call.answer()

# изменяем поле после хода бота
def new_keyboard_bot(num):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    del buttons[num]
    buttons.insert(num, types.InlineKeyboardButton(text=symbol_o, callback_data=callback_numbers.new(num=str(num))))
    keyboard.add(*buttons)
    restart_game = types.InlineKeyboardButton(text='Начать заново', callback_data='restart')
    keyboard.add(restart_game)
    return keyboard

# ход бота, если поле пустое, то меняем его на О
async def play_bot(call: types.CallbackQuery, callback_data: dict):
    game_bot = random.randint(0, 8)
    if buttons[game_bot]['text'] == symbol_undef:
        await call.message.edit_reply_markup(reply_markup=new_keyboard_bot(game_bot))
        with suppress(MessageNotModified):
            if await is_win(call, buttons, symbol_o):
                await call.answer(text='Ты проиграл\U0001F635\U0001F635\U0001F635, удачи в новой партии!', show_alert=True)
                return
    else:  # через while True не хотел выводить сообщение, сообщение то выскакивало, то нет.
        await play_bot(call, callback_data)
    await play_player(call, callback_data)
    await call.answer()

# функция проверки победителя
async def is_win(call, list_, symbol):
    if ((list_[0]['text'] == symbol and list_[1]['text'] == symbol and list_[2]['text'] == symbol) or (
            list_[3]['text'] == symbol and list_[4]['text'] == symbol and list_[5]['text'] == symbol) or (
            list_[6]['text'] == symbol and list_[7]['text'] == symbol and list_[8]['text'] == symbol) or (
            list_[0]['text'] == symbol and list_[3]['text'] == symbol and list_[6]['text'] == symbol) or (
            list_[1]['text'] == symbol and list_[4]['text'] == symbol and list_[7]['text'] == symbol) or (
            list_[2]['text'] == symbol and list_[5]['text'] == symbol and list_[8]['text'] == symbol) or (
            list_[0]['text'] == symbol and list_[4]['text'] == symbol and list_[8]['text'] == symbol) or (
            list_[2]['text'] == symbol and list_[4]['text'] == symbol and list_[6]['text'] == symbol)):
        return True
    return False

# функция для определения ничьи
async def is_draw(call, list_):
    count = 0
    for key, value in enumerate(list_):
        for i in value['text']:
            if i != symbol_undef:
                count += 1
    if count == 9:
        return True
    else:
        return False

# рестарт игры
@dp.callback_query_handler(text=['restart'])
async def restart_ttt(call: types.CallbackQuery):
    global buttons
    buttons = []
    await create_keyboard(call.message)

########################################################################################################################
########################################################################################################################
########################################################################################################################

# Раздел о погоде
@dp.message_handler(commands=['weather_city'], state=None)
async def start_weather(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, введи название города '
                                                      f'и я покажу тебе информацию о погоде')
    await User_step.weather_user.set()


@dp.message_handler(state=User_step.weather_user)
async def get_weather(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    take = data['city']
    if take.isalpha():
        try:
            ct = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={message.text}&appid={open_weather_token}')
            coord = ct.json()
            coord_lat = coord[0]['lat']
            coord_lon = coord[0]['lon']

            r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coord_lat}&lon={coord_lon}&appid={open_weather_token}&units=metric&lang=ru')
            data = r.json()
            city = data['name']
            cur_weather = data['main']['temp']

            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
            len_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.\
                fromtimestamp(data['sys']['sunrise'])


            await message.answer(f'Погода в городе: {city} \nТемпература: {cur_weather} C°\n'
                                 f'Влажность: {humidity}% \nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с \n'
                                 f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
                                 f'Продолжительность дня: {len_of_the_day}\n'
                                 f'\n \U0001F91F Хорошего дня тебе мой друг!\n'
                                 f'\nЕсли хочешь узнать погоду в другом городе, выбери в меню нужную команду \U0001F642 ')
        except:
            await message.answer('Проверь название города')
            await get_weather(message, FSMContext)
    else:
        await message.answer('Проверь название города')
        await get_weather(message, FSMContext)
    await state.finish()


########################################################################################################################
########################################################################################################################
########################################################################################################################


