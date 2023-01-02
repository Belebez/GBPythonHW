# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random


k_1 = int(input("Для первого выражения, введите натуральную степень k = "))
k_2 = int(input("Для второго выражения, введите натуральную степень k = "))

# функция создания выражения многочлена
def create_eq(k):
    koef = {}
    for i in range(k + 1):
        koef[i] = random.randint(-100, 101)

    equation = ''
    for i in range(k, -1, -1):
        if koef[i] > 0:
            if koef[i] == 1:
                if i == 1:
                    equation += f'x +'
                elif i == 0:
                    equation += f'1 '
                else:
                    equation += f'x**{i} +'
            else:
                if i == 1:
                    equation += f' {koef[i]}*x +'
                elif i == 0:
                    equation += f' {koef[i]} '
                else:
                    equation += f' {koef[i]}*x**{i} +'
        elif koef[i] < 0:
            if koef[i] == -1:
                if i == 1:
                    equation = f'{equation[:-1]}- x +'
                elif i == 0:
                    equation = f'{equation[:-1]}- 1 '
                else:
                    equation = f'{equation[:-1]}- x**{i} +'
            else:
                if i == 1:
                    equation = f'{equation[:-1]}- {abs(koef[i])}*x +'
                elif i == 0:
                    equation = f'{equation[:-1]}- {abs(koef[i])} '
                else:
                    equation = f'{equation[:-1]}- {abs(koef[i])}*x**{i} +'
    return equation.lstrip() + "= 0"

# функция записи в файл
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


# записываем полученные многочлен в файл
write_file('task11.txt', create_eq(k_1))
write_file('task12.txt', create_eq(k_2))

# вывод выражения в консоль
with open('task11.txt', 'r') as data:
    eq_1 = data.readlines()
with open('task12.txt', 'r') as data:
    eq_2 = data.readlines()
print()
print('Выражение первого многочлена:', *eq_1)
print('Выражение второго многочлена:', *eq_2)


def decode(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ').replace(' 1*x', ' x').replace('*x**0', '').replace('x**1', 'x')
    return new_equation

def encode(equation: str) -> dict:
    equation = equation.replace(' + ', ' ').replace('- ', '-').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x').replace('*x ', '*x**1 ').split()
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        elif len(i) == 1:
            dict_equation[0] = int(i[0])
    return dict_equation

# # получение степени многочлена
# def degree_mn(eq):
#     if 'x**' in eq:
#         i = eq.find('**')
#         degree_num = int(eq[i + 2:i + 3])
#     elif ('x' in eq) and ('**' not in eq):
#         degree_num = 1
#     else:
#         degree_num = -1
#     return degree_num
#
# # получение коэфф многочлена
# def koef_mn(eq):
#     if 'x' in eq:
#         i = eq.find('x')
#         koef_num = int(eq[:i - 1])
#     return koef_num

# функция сложения выражений
def addition(eq_1: dict, eq_2: dict):
    final_eq = {}
    final_eq.update(eq_1)
    final_eq.update(eq_2)
    for key in final_eq:
        final_eq[key] = eq_1.get(key, 0) + eq_2.get(key, 0)
    return final_eq

# применяем функции и получаем конечное выражение
eq_1 = ' '.join(eq_1)
eq_1 = eq_1[:-4]
eq_2 = ' '.join(eq_2)
eq_2 = eq_2[:-4]
eq_1 = encode(eq_1)
eq_2 = encode(eq_2)
final_eq = addition(eq_1, eq_2)
final_eq = decode(final_eq)
print()
print(f'Выражение, полученное после сложения двух многочленов : {final_eq}')




