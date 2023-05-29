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

    def start(self):
        model = self.__model
        view = self.__view
        while True:
            match view.main_menu(text.main_menu, range(1, 8)):
                case 1:
                    pb_filename = view.read_pb_file_name(text.enter_contact_filename).strip()
                    if not pb_filename:
                        pb_filename = "contacts.txt"
                    if model.opened() and not model.saved():#проверяем на то, был ли открыт справочник и не был ли он сохранён
                        if view.ask_yes_no_question_from_user(text.need_to_save_pb_file):#сохраняем, если пользователь ответил да
                            model.save()
                    model.open(pb_filename)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    break
