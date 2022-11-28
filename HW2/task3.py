# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
print("Программа создаёт случайный список и перемешивает элементы случайным образом, без использования встроенного метода Shuffle().")
print()

from random import randint as rnd

size = int(rnd(4, 10))
list = []
for i in range(size):
    list.append(rnd(0, 100))
print(f'Полученный список - {list}')

for i in range(len(list) - 1, 0, -1):
    rnd_index = rnd(0, i)
    list[i], list[rnd_index] = list[rnd_index], list[i]
print(f'Перемешанный список - {list}')
