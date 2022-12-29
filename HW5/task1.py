# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint

print('Программа для игры с конфетами, человек против компьютера. На столе лежит 150 конфет. Побеждает тот, кто забрал последние конфеты.\n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
print()

def human_quantity(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def bot_quantity(value):
    move_bot = randint(1, 28)
    while value-move_bot <= 28 and value > 29:
        move_bot = randint(1, 28)
    return move_bot



def print_console(name, quantity, counter, value):
    print(
        f"Ходил {name}, он взял {quantity}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = 'Человек'
player2 = "Бот"
value = 150
counter1 = 0
counter2 = 0

flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


while value > 28:
    if flag:
        quantity = human_quantity(player1)
        counter1 += quantity
        value -= quantity
        flag = False
        print_console(player1, quantity, counter1, value)
    else:
        quantity = bot_quantity(value)
        counter2 += quantity
        value -= quantity
        flag = True
        print_console(player2, quantity, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
