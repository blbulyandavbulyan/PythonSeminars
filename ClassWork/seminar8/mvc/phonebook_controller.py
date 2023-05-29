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
    def __save_if_yes(self):
        if self.__view.ask_yes_no_question_from_user(
                text.need_to_save_pb_file):  # сохраняем, если пользователь ответил да
            self.__model.save()

    def start(self):
        model = self.__model
        view = self.__view
        if not model.opened():
            self.__open_pb()
        while True:
            match view.main_menu(text.main_menu, range(1, 9)):
                case 1:
                    if model.opened() and not model.is_pb_saved():  # проверяем на то, был ли открыт справочник и не был ли он сохранён
                        self.__save_if_yes()
                    self.__open_pb()
                case 2:
                    model.save()
                case 3:
                    view.print_contacts(model.get_contacts(), text.phonebook_is_empty)
                case 4:
                    new_contact = view.read_new_contact(text.messages_for_parts_of_contact)
                    model.add(new_contact)
                case 5:
                    found_contacts = model.find(view.read_search_line(text.enter_string_to_search))
                    view.print_contacts(found_contacts, text.contact_not_found_by_your_query)
                case 6:
                    while True:
                        contact_id_to_modify = view.read_contact_id(text.enter_contact_id_to_modify, model.contains_id)
                        if contact_id_to_modify == -1:
                            break
                        elif model.contains_id(contact_id_to_modify):
                            model.modify(contact_id_to_modify,
                                         view.read_modified_contact(
                                             model.get(contact_id_to_modify), text.messages_for_parts_of_contact
                                         )
                                         )
                            break
                case 7:
                    while True:
                        contact_id_to_delete = view.read_contact_id(text.enter_contact_id_to_delete, model.contains_id)
                        if contact_id_to_delete == -1:
                            break
                        elif model.contains_id(contact_id_to_delete):
                            model.delete(contact_id_to_delete)
                            break
                    pass
                case 8:
                    if not model.is_pb_saved():
                        self.__save_if_yes()
                    break
