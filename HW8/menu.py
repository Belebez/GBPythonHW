import view
import data_base as db
import phone_book as pb


def main_menu(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_phone_book()
            view.show_phone_book(phone_book)
        case 2:
            db.read_data_base()
            view.download_completed()
        case 3:
            db.save_phone_book()
            view.save_completed()
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5:
            pb.change_contact(view.input_change_contact())
            view.change_completed()
        case 6:
            phone_book = pb.get_phone_book()
            view.show_phone_book(phone_book)
            id = view.input_delete_contact()
            if pb.delete_contact(id):
                view.delete_completed()
        case 7:
            str_search = view.input_find_contact()
            pb.find_contact(str_search)
        case 0:
            return True


def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break
