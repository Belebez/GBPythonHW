phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book
    return phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def change_contact(new_contact: list):
    global phone_book
    for i in range(len(phone_book[new_contact[0] - 1])):
        if new_contact[i + 1] != '':
            del phone_book[new_contact[0] - 1][i]
            phone_book[new_contact[0] - 1].insert(i, new_contact[i + 1])

def delete_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}?(y/n) -> ')
    if confirm.lower() == 'y':
        del phone_book[id - 1]
        return True
    return False

def find_contact(str_search: str):
    global phone_book
    count = 0
    for i in range(len(phone_book)):
        for j in phone_book[i]:
            if str_search in j:
                print()
                print(*phone_book[i])
                count += 1
    if count == 0:
        print('\nТакого словосочетания нет ни в одних полях книги.')

