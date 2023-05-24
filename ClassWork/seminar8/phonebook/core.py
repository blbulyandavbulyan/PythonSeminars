from typing import Tuple


# данный файл содержит ядро телефонного справочника, все функции которые находятся здесь не  требуют от пользователя
# ввода данных с клавиатуры В качестве структуры для хранения справочника используется словарь с ключом по id (целое
# число) и значением в виде кортежа из: ФИО, номера телефона и комментария
# В файле справочник сохраняется в следующем формате:
# Каждый контакт с новой строки и записывается так: id;fio;phone;comment
# где id - ид контакта, целочисленный(не может быть -1!!!)
# fio - Фамилия Имя Отчество (записанные через пробел)
# phone - телефон
# comment - Комментарий
# Все точки запятой содержащиеся в кортеже строк, описывающий контакт при добавлении его в книгу будут проигнорированы,
# дабы избежать неправильной записи в файл
class InvalidContactIdInFile(RuntimeError):  # исключение, бросаемое в случае если в файле есть контакт с ид -1
    pass


def save(pb: dict[int, Tuple[str, str, str]], filename: str):
    with open(filename, "w") as output_file:
        for k, v in pb:
            output_file.write(f'{k};{v[0]};{v[1]};{v[2]}\n')


def load(filename: str) -> dict[int, Tuple[str, str, str]]:
    result = dict()
    with open(filename, "r") as input_file:
        for line in input_file:
            (contact_id, fio, phone, comment) = map(lambda s: s.strip(), line.split(";"))
            if contact_id == -1:
                # по хорошему, тут должно бросаться исключение, но мы же не проходили, поэтому
                raise InvalidContactIdInFile(f"ИД контакта не может быть -1 в файле {filename}")
            result[int(contact_id)] = (fio, phone, comment)
    return result


def find_contact(pb: dict[int, Tuple[str, str, str]], find_str: str) -> int:
    find_str = find_str.lower()
    for k, v in pb.items():
        if v[0].lower().find(find_str) != -1 or v[1].lower().find(find_str) != -1 or v[2].lower().find(
                find_str) != -1:  # заменить на проверку подстрок
            return k
    return -1


def get_formatted_contact_str(contact: Tuple[int, Tuple[str, str, str]]) -> str:
    contact_id = contact[0]
    fio, phone, comment = contact[1]
    return f'{contact_id} {fio}:\n\tТелефон: {phone}\n\tКомментарий: {comment}'


def print_contacts(pb: dict[int, Tuple[str, str, str]]) -> None:
    for k, v in pb.items():
        print(get_formatted_contact_str((k, v)))


def add_contact(pb: dict[int, Tuple[str, str, str]], contact: Tuple[str, str, str]) -> None:
    current_id = max(pb.keys())
    fio, phone, comment = map(lambda x: x.replace(";", ""), contact)
    pb[current_id + 1] = (fio, phone, comment)


def delete_contact(pb: dict[int, Tuple[str, str, str]], contact_id: int) -> None:
    pb.pop(contact_id)
