# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
from random import randint as rnd

print("Программа преобразует десятичное число в двоичное.")
print()

num_decimal = int(rnd(0, 100))
print(f'Десятичное число {num_decimal},', end=' ')
binary = ''

while num_decimal > 0:
    binary = str(num_decimal % 2) + binary
    num_decimal //= 2

print(f'в двоичной системе выглядит как - {binary}')