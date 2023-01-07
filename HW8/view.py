


def main_menu():
    print('\n1. Показать телефонную книгу ')
    print('2. Открыть телефонную книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print()
    print('0. Выход\n')
    return choice_main_menu()

def choice_main_menu():
    while True:
        try:
            choice = int(input('Введите нужный пункт из меню: '))
            if choice in range(0, 8):
                return choice
            else:
                print('\nТакого пункта в меню нет.\n')
        except:
            print('\nНекорректный ввод, попробуйте еще раз.\n')

def log_off():
    print('\nДо свидания, до новых встреч!')

def download_completed():
    print('\nТелефонная книга загружена.')

def save_completed():
    print('\nТелефонная книга сохранена.')

def change_completed():
    print('\nКонтакт изменён.')

def delete_completed():
    print('\nКонтакт удалён.')

def show_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, name in enumerate(phone_book, 1):
            print(id, *name)
    else:
        print('\nТелефонная книга пуста или не загружена.')

def input_new_contact():
    name = input('\nВведите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий для контакта: ')
    return [name, phone, comment]

def input_change_contact():
    id = int(input('\nВведите ID контакта, который вы хотите изменить: '))
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон контакта: ')
    comment = input('Введите новый комментарий для контакта: ')
    return [id, name, phone, comment]

def input_delete_contact():
    id = int(input('Введите ID контакта, которого вы хотите удалить: '))
    return id

def input_find_contact():
    str_search = input('\nВведите "параметры" для поиска: ')
    return str_search