# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
from math import *

print('Программа, принимает на вход на вход координаты двух точек и находит расстояние между ними. ')
print()

flag = False

while flag != True:

    coords = input('Введите координаты двух точек через пробел: ').split(' ')

    if len(coords) / 2 == 2:
        x1, x2 = int(coords[0]), int(coords[2])
        y1, y2 = int(coords[1]), int(coords[3])
        distance = round((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)), 2)
        print(f'Расстояние в 2D пространстве между точками А[{x1}, {y1}] и В[{x2}, {y2}] равно {distance}')
    elif len(coords) / 2 == 3:
        x1, x2 = int(coords[0]), int(coords[3])
        y1, y2 = int(coords[1]), int(coords[4])
        z1, z2 = int(coords[2]), int(coords[5])
        distance = round((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)), 2)
        print(f'Расстояние в 3D пространстве между точками А[{x1}, {y1}, {z1}] и В[{x2}, {y2}, {z2}] равно {distance}')
    else:
        print('Введены неверные координаты.')

    print()
    replay = input('Попробуете еще раз?(да/нет): ')
    # создаём условия для повтора или выхода из программы
    if replay.lower() == 'да' or replay.lower() == 'yes':
        flag = False
    else:
        flag = True
