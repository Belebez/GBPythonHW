# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

print("Программа находит произведение пар элементов списка. Пара считается первый и и последний элемент, второй и предпоследний и тд.")
print()

from random import randint as rnd

size = int(rnd(4, 10))
list = []
for i in range(size):
    list.append(rnd(0, 100))
print(f'Дан список - {list}')

list1 = []
prod_num = 1
if len(list) % 2 == 0:
    for i in range(0, (int(len(list) / 2))):
        prod_num = list[i] * list[((len(list) - 1) - i)]
        list1.append(prod_num)
        print(f'Произведение элементов {list[i]} и {list[((len(list) - 1) - i)]} равно {prod_num} ')
else:
    for i in range(0, (int(len(list) / 2) + 1)):
        prod_num = list[i] * list[((len(list) - 1) - i)]
        list1.append(prod_num)
        print(f'Произведение элементов {list[i]} и {list[((len(list) - 1) - i)]} равно {prod_num} ')

print()
print(f'Список произведения элементов - {list1}')