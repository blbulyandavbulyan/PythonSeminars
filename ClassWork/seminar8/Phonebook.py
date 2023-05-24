# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
# Поля: ФИО, телефон, комментарий
from typing import Tuple
from phonebook import core as pb_core

def load_pb_from_typed_filename() -> (str, dict[int, Tuple[str, str, str]]):
    filename = input('Введите имя файла с контактами(оставьте пустым для варианта по умолчанию): ')
    if len(filename) == 0:
        filename = "contacts.txt"
    return pb_core.load(filename)
def do_action_if_input_valid_contact_id(pb: dict[int, Tuple[str, str, str]])

def menu() -> None:
    filename, phonebook = load_pb_from_typed_filename()
    print("""
            1. Открывать другой файл
            2. Сохранить файл
            3. Показать все контакты
            4. Добавить контакт
            5. Найти контакт
            6. Изменить контакт
            7. Удалить контакт
            8. Выход
        """)
    stopped = False
    while not stopped:
        match input('Введите действие: '):
            case '1':
                filename, phonebook = load_pb_from_typed_filename()
            case '2':
                pb_core.save(phonebook, filename)
            case '3':
                pb_core.print_contacts(phonebook)
            case '4':
                read_contact_and_add(phonebook)
            case '5':
                finded_id = pb_core.find_contact(phonebook, input('Введите подстроку для поиска: '))
                print(pb_core.get_formatted_contact_str(phonebook[finded_id]) if finded_id != -1 else 'Контакт не найден')
            case '6':
                contact_id_for_modify = int(input('Введите ИД контакта для изменения: '))
                if contact_id_for_modify in phonebook:
                    modify_contact(phonebook, contact_id_for_modify)
                else:
                    print('Контакта с таким ИД в справочнике нет')
            # case '7':
                # pb_core.delete_contact(phonebook, )





def modify_contact(pb: dict[int, Tuple[str, str, str]], contact_id: int) -> None:
    print('Выберите что вы хотите изменить?\n\t1)ФИО\n\t2)Телефон\n\t3)Комментарий')
    fio, phone, comment = pb[contact_id]
    variants = input()
    for variant in variants:
        match variant:
            case '1':
                fio = input('Введите новое ФИО: ')
            case '2':
                phone = input('Введите новый телефон: ')
            case '3':
                comment = input('Введите новый комментарий: ')
    fio.replace(";", "")
    phone.replace(";", "")
    comment.replace(";", "")
    pb[contact_id] = (fio, phone, comment)

def read_contact_and_add(pb: dict[int, Tuple[str, str, str]]) -> None:
    fio = input('Введите ФИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    add_contact(pb, (fio, phone, comment))


if __name__ == '__main__':
    pb = {1: ("Иванов Иван Иванович", "89192421216", "Какой-то комментарий"),
          2: ("Петров Петр Петрович", "892342421216", "Что-то другое")}
    read_contact_and_add(pb)
    print_contacts(pb)
    id = find_contact(pb, input('Введите ключевое слово для поиска контакта: '))
    print(id)
    modify_contact(pb, id)
    print_contacts(pb)
