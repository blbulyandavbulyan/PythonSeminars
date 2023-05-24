import os.path
from typing import Callable


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


class Contact(object):
    def __init__(self, fio: str, phone: str, comment: str):
        self.__fio = fio.replace(";", "")
        self.__phone = phone.replace(";", "")
        self.__comment = comment.replace(";", "")

    def __contains__(self, item: str) -> bool:
        item_cf = item.casefold()
        return item_cf in self.__fio.casefold() or item_cf in self.__phone or item_cf in self.__comment

    @property
    def file_data(self) -> str:
        return f'{self.__fio};{self.__phone};{self.__comment}\n'

    @property
    def fio(self):
        return self.__fio

    @property
    def phone(self):
        return self.__phone

    @property
    def comment(self):
        return self.__comment


def get_formatted_contact_str(contact_id: int, contact: Contact) -> str:
    return f'{contact_id} {contact.fio}\n'


class PhoneBook(object):
    __pb: dict[int, Contact] = dict()
    __filename: str = "contacts.txt"

    def __init__(self, filename="contacts.txt"):
        self.__filename = filename
        if os.path.exists(filename):
            with open(filename, "r") as input_file:
                for line in input_file:
                    (contact_id, fio, phone, comment) = map(lambda s: s.strip(), line.split(";"))
                    if contact_id == -1:
                        raise InvalidContactIdInFile(f"ИД контакта не может быть -1 в файле {filename}")
                    self.__pb[int(contact_id)] = Contact(fio, phone, comment)

    def save(self):
        with open(self.__filename, "w") as output_file:
            for contact_id, contact in self.__pb.items():
                output_file.write(f'{contact};{contact.file_data}')

    def find_contact(self, find_str: str) -> int:
        find_str = find_str.lower()
        for contact_id, contact in self.__pb.items():
            if find_str in contact:
                return contact_id
        return -1

    #
    #
    #
    # def print_contacts(self) -> None:
    #     for k, v in self.__pb.items():
    #         print(get_formatted_contact_str((k, v)))
    def foreach(self, consumer: Callable[[int, Contact], None]):
        for contact_id, contact in self.__pb.items():
            consumer(contact_id, contact)

    def add(self, contact: Contact) -> int:
        current_id = max(self.__pb.keys())
        self.__pb[current_id + 1] = contact
        return current_id

    def delete(self, contact_id: int) -> Contact:
        return self.__pb.pop(contact_id)
