# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print('Программу, принимает на вход вещественное число и показывает сумму его цифр.')
print()

num = float(input('Введите вещественное число: '))

if num == int(num):
    sum_num = 0
    while num > 0:
        sum_num += (int(num % 10))
        num //= 10
    print(f'Сумма цифр в числе равна {sum_num}')
else:
    sum_num = 0
    num = str(num).split('.')
    num1 = int(num[0])
    num2 = int(num[1])
    while num1 > 0:
        sum_num += (int(num1 % 10))
        num1 //= 10
    while num2 > 0:
        sum_num += (int(num2 % 10))
        num2 //= 10
    print(f'Сумма цифр в числе равна {sum_num}')


