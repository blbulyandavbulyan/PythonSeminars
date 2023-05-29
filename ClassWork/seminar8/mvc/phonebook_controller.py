import text
from mvc.phonebook_model import PhoneBookModel
from mvc.phonebook_view import PhoneBookView


# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

class PhoneBookController:
    def __init__(self, view: PhoneBookView, model: PhoneBookModel):
        self.__view = view
        self.__model = model

    def __open_pb(self):
        pb_filename = self.__view.read_pb_file_name(text.enter_contact_filename).strip()
        if not pb_filename:
            pb_filename = "contacts.txt"
        self.__model.open(pb_filename)

    def start(self):
        model = self.__model
        view = self.__view
        if not model.opened():
            self.__open_pb()
        while True:
            match view.main_menu(text.main_menu, range(1, 8)):
                case 1:
                    if model.opened() and not model.saved():  # проверяем на то, был ли открыт справочник и не был ли он сохранён
                        if view.ask_yes_no_question_from_user(
                                text.need_to_save_pb_file):  # сохраняем, если пользователь ответил да
                            model.save()
                    self.__open_pb()
                case 2:
                    model.save()
                case 3:
                    view.print_contacts(model.get_contacts(), text.phonebook_is_empty)
                case 4:
                    new_contact = view.read_new_contact(text.new_contact_messages)
                    model.add(new_contact)
                case 5:
                    found_contacts = model.find(view.read_search_line(text.enter_string_to_search))
                    view.print_contacts(found_contacts, text.contact_not_found_by_your_query)
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    break
