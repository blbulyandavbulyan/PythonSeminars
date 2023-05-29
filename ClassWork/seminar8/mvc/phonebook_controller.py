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
        while True:
            match self.__view.main_menu(text.main_menu, range(1, 8)):
                case 1:
                    pass
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
