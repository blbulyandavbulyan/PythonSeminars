# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
# Поля: ФИО, телефон, комментарий
# 1; Иванов Иван Иванович; 89192421216; Какой-то комментарий
from typing import Tuple


def load_pb_from_typed_filename() -> (str, dict[int, Tuple[str, str, str]]):
    filename = input('Введите имя файла с контактами(оставьте пустым для варианта по умолчанию): ')
    if len(filename) == 0:
        filename = "contacts.txt"
    return load_pb(filename)


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
    match input('Введите действие: '):
        case '1':
            filename_phonebook = load_pb_from_typed_filename()
        case '2':
            save_pb(phonebook, filename)
        case '3':
            print_contacts(phonebook)
        case '4':
            read_contact_and_add(phonebook)
        case '5':
            finded_id = find_contact(phonebook, input('Введите подстроку для поиска: '))
            print(get_formated_contact_str(phonebook[finded_id]) if finded_id != -1 else 'Контакт не найден')
        case '6':
            contact_id_for_modify = int(input('Введите ИД контакта для изменения: '))
            if contact_id_for_modify in phonebook:
                modify_contact(phonebook, contact_id_for_modify)
            else:
                print('Контакта с таким ИД в справочнике нет')
def save_pb(pb: dict[int, Tuple[str, str, str]], filename: str):
    with open(filename, "w") as output_file:
        for k, v in pb:
            output_file.write(f'{k};{v[0]};{v[1]};{v[2]}\n')


def load_pb(filename: str) -> dict[int, Tuple[str, str, str]]:
    result = dict()
    with open(filename, "r") as input_file:
        for line in input_file:
            (id_, fio, phone, comment) = map(lambda s: s.strip(), line.split(";"))
            result[int(id_)] = (fio, phone, comment)
    return result


def find_contact(pb: dict[int, Tuple[str, str, str]], find_str: str) -> int:
    find_str = find_str.lower()
    for k, v in pb.items():
        if v[0].lower().find(find_str) != -1 or v[1].lower().find(find_str) != -1 or v[2].lower().find(
                find_str) != -1:  # заменить на проверку подстрок
            return k
    return -1


def get_formated_contact_str(contact: Tuple[int, Tuple[str, str, str]]) -> str:
    id = contact[0]
    fio, phone, comment = contact[1]
    return f'{id} {fio}:\n\tТелефон: {phone}\n\tКомментарий: {comment}'


def print_contacts(pb: dict[int, Tuple[str, str, str]]) -> None:
    for k, v in pb.items():
        print(get_formated_contact_str((k, v)))


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


def add_contact(pb: dict[int, Tuple[str, str, str]], contact: Tuple[str, str, str]) -> None:
    current_id = max(pb.keys())
    pb[current_id + 1] = contact


def delete_contact(pb: dict[int, Tuple[str, str, str]], contact_id: int) -> None:
    pb.pop(contact_id)


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
