# Данный файл содержит текстовые строки или функции, которые их генерируют.
# Используется в местах где нужно вывести текст пользователю.
from textwrap import dedent

main_menu = '''\nГлавное меню: 
    1. Открывать другой файл
    2. Сохранить файл
    3. Показать все контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''
enter_contact_filename = 'Введите имя файла с контактами(оставьте пустым для варианта по умолчанию): '
need_to_save_pb_file = 'Вы не сохранили уже открытый справочник хотите сохранить ?(y/n): '
phonebook_is_empty = 'Список контактов пуст!'
messages_for_parts_of_contact = {"fio": "Введите ФИО: ", "phone": "Введите телефон: ", "comment": "Введите комментарий: "}
enter_string_to_search = "Введите строку для поиска: "
contact_not_found_by_your_query = 'По вашему запросу контакты не найдены'
enter_contact_id_for = "Введите ИД контакта для "
enter_contact_id_to_modify = f"{enter_contact_id_for} изменения: "
enter_contact_id_to_delete = f"{enter_contact_id_for} удаления: "
enter_your_choice = "Введите вариант: "
leave_blank_to_not_change = "Оставьте пустыми те данные, которые не хотите менять"
you_enter_not_a_integer_number = "Вы ввели не целое число!"
phonebook_does_not_contain_given_contact_id = "Справочник не содержит введённого ИД контакта!"
