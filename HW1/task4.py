# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
print()

flag = False

while flag != True:

    quarter = input('Введите номер четверти: ')

    if quarter == '1' or quarter == 'I':
        print(f'Диапазон возможных координат точек в {quarter} четверти x > 0 и y > 0')
    elif quarter == '2' or quarter == 'II':
        print(f'Диапазон возможных координат точек в {quarter} четверти x < 0 и y > 0')
    elif quarter == '3' or quarter == 'III':
        print(f'Диапазон возможных координат точек в {quarter} четверти x < 0 и y < 0')
    elif quarter == '4' or quarter == 'IV':
        print(f'Диапазон возможных координат точек в {quarter} четверти x > 0 и y < 0')
    else:
        print('Такой четверти нет.')

    print()
    replay = input('Попробуете еще раз?(да/нет): ')
    # создаём условия для повтора или выхода из программы
    if replay.lower() == 'да' or replay.lower() == 'yes':
        flag = False
    else:
        flag = True
