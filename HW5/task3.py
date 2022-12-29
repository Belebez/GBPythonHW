# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

print('Программа реализует модуль сжатия и восстановления данных.\n'
      'Принимает на вход выражение "ааfffcccc" на выходе "2a3f4c" или наоборот.')
print()


cipher = input('Введите текст для преобразования: ')


def rle_decoder(text):
    decoding = ''
    number = ''
    count = 1
    if text.isalpha() == True:
        for i in range(len(text) - 1):
            if text[i] == text[i + 1]:
                count += 1
            else:
                decoding += str(count) + text[i]
                count = 1
        if count > 1 or (text[len(text) - 2] != text[-1]):
            decoding += str(count) + text[-1]
        return decoding
    elif text.isalnum() == True:
        for i in range(len(text)):
            if text[i].isalpha() == False:
                number += text[i]
            else:
                decoding += text[i] * int(number)
                number = ''
        return decoding
    else:
        return 'Ввели неверное выражение.'

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

write_file('task3in.txt', cipher)
write_file('task3out.txt', rle_decoder(cipher))