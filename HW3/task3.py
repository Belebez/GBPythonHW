# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from random import randint as rnd

print("Программа создаёт список из вещественных чисел. Находит разницу между максимальным и минимальным значением дробной части. ")
print()

size = int(rnd(4, 10))
list = []
for i in range(size):
    list.append(round(random.uniform(0, 100), 2))
print(f'Дан список - {list}')

list_fract_part = []
for i in list:
    if i != int(i):
        i = str(i).split('.')
        list_fract_part.append(int(i[1]))

print(f'Максимальное значение дробной части -  {max(list_fract_part) / 100} \n'
      f'Минимальное значение дробной части -  {min(list_fract_part) / 100} \n'
      f'Разница этих значений - {(max(list_fract_part) - min(list_fract_part)) / 100}')