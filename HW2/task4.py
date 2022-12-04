# # Написать программу, которая состоит 4 из этапов:
# # - создает список из рандомных четырех значных чисел
# # - принимает с консоли цифру и удаляет ее из всех элементов списка
# # - цифры каждого элемента суммирует пока результат не станет однозначным числом
# # - из финального списка убирает все дублирующиеся элементы
# # - после каждого этапа выводить результат в консоль
# # Пример:
# # - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# # - 2 этап: Введите цифру: 3
# # - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# # - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# # - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# # - 4 этап: [3, 1, 5, 4]

from random import randint as rnd

print("1 этап. Программа создаст список из случайных четырехзначных чисел.")

size = int(rnd(4, 10))
list = []
for i in range(size):
    list.append(rnd(1000, 9999))
print(f'1 этап: - {list}')
print()
print("2 этап. Программа примет от пользователя цифру и удалит ее из всех элементов ранее созданного списка.")

sub_text = input('Введите число: ')
new_list2 = []

for i in range(len(list)):
    words = str(list[i])
    result_str = ''
    for j in range(len(words)):
        if words[j] != sub_text:
            result_str += str(words[j])
    new_list2.append(int(result_str))
print(f'2 этап: - {new_list2}')

print()
print("3 этап. Программа суммирует цифры каждого элемента пока результат не станет однозначным числом.")

new_list3 = []

# решил использовать рекурсию, так как одним циклом не посчитаешь, и даже двумя, чтобы не плодить код
def sum_num(num):
    if num == 0: return 0
    return num % 10 + sum_num(num // 10)

for i in new_list2:
    number = sum_num(i)
    if number > 9:
        number1 = sum_num(number)
        if number1 > 9:
            number2 = sum_num(number1)
            new_list3.append(number2)
        else:
            new_list3.append(number1)
    else:
        new_list3.append(number)
print(f'3 этап: - {new_list3}')

print()
print("4 этап. Программа удаляет дублирующие элементы.")

new_list4 = []

for i in new_list3:
    if i not in new_list4:
        new_list4.append(i)
print(f'4 этап: - {new_list4}')