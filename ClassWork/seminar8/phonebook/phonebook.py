import os.path
from typing import Callable

from phonebook.contact import Contact, BaseContact


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
class PhoneBookException(RuntimeError):
    pass


class ValueIsNotContact(PhoneBookException):
    pass


class NoContactWithGivenContactId(PhoneBookException):
    pass


class PhoneBook(object):
    __pb: dict[int, Contact] = dict()
    __filename: str = "contacts.txt"

    def __init__(self, filename="contacts.txt"):
        self.__filename = filename
        if os.path.exists(filename):
            with open(filename, "r") as input_file:
                for line in input_file:
                    (contact_id, fio, phone, comment) = map(lambda s: s.strip(), line.split(";"))
                    contact_id = int(contact_id)
                    if contact_id == -1:
                        self.__pb[int(contact_id)] = Contact(contact_id, fio, phone, comment)

    def __getitem__(self, item: int) -> Contact:
        return self.__pb[item]

    def __setitem__(self, key: int, value: BaseContact) -> None:
        if key in self.__pb:
            if isinstance(value, BaseContact):
                # такая сложная вещь нужна чтобы сохранить старый id
                self.__pb[key] = Contact(key, value.fio, value.phone, value.comment)
            else:
                raise ValueIsNotContact("Вы пытаетесь записать в книгу с контактами не контакт!")
        else:
            raise NoContactWithGivenContactId("Нет контакта с переданным id!")

    def __contains__(self, item: int):
        return item in self.__pb

    def save(self):
        with open(self.__filename, "w") as output_file:
            for contact_id, contact in self.__pb.items():
                output_file.write(f'{contact.file_data}\n')

    def find(self, find_str: str) -> list[Contact]:
        find_str = find_str.lower()
        return [contact for contact in self.__pb.values() if find_str in contact]

    def foreach(self, consumer: Callable[[Contact], None]):
        for contact in self.__pb.values():
            consumer(contact)

    def add(self, contact: Contact) -> int:
        current_id = max(self.__pb.keys())
        self.__pb[current_id + 1] = contact
        return current_id

    def delete(self, contact_id: int) -> Contact:
        return self.__pb.pop(contact_id)
