# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
# Поля: ФИО, телефон, комментарий
from mvc.phonebook_console_view import PhoneBookConsoleView
from mvc.phonebook_controller import PhoneBookController
from phonebook.phonebook import PhoneBook


if __name__ == '__main__':
    PhoneBookController(PhoneBookConsoleView(), PhoneBook()).start()
