import os.path
from abc import ABC
from typing import Callable, Iterable

from mvc.phonebook_model import PhoneBookModel
from phonebook.contact import Contact, BaseContact


# данный файл содержит ядро телефонного справочника, все функции которые находятся здесь не  требуют от пользователя
# ввода данных с клавиатуры В качестве структуры для хранения справочника используется словарь с ключом по id (целое
# число) и значением в виде кортежа из: ФИО, номера телефона и комментария
# В файле справочник сохраняется в следующем формате:
# Каждый контакт с новой строки и записывается так: id;fio;phone;comment
# где id - ид контакта, целочисленный(не может быть меньше чем 1!!!)
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


class PhoneBook(PhoneBookModel):

    def __init__(self):
        self.__filename = "contacts.txt"
        self.__pb = dict()
        self.__saved = True
        self.__opened = False

    def __getitem__(self, item: int) -> Contact:
        return self.__pb[item]

    def __setitem__(self, key: int, value: BaseContact) -> None:
        if key in self.__pb:
            if isinstance(value, BaseContact):
                # такая сложная вещь нужна чтобы сохранить старый id
                self.__pb[key] = Contact(key, value.fio, value.phone, value.comment)
                self.__saved = False
            else:
                raise ValueIsNotContact("Вы пытаетесь записать в книгу с контактами не контакт!")
        else:
            raise NoContactWithGivenContactId("Нет контакта с переданным id!")

    def __contains__(self, item: int):
        return item in self.__pb

    def __len__(self):
        return len(self.__pb)

    @property
    def saved(self) -> bool:
        return self.__saved

    def save(self):
        with open(self.__filename, "w") as output_file:
            for contact_id, contact in self.__pb.items():
                output_file.write(f'{contact.file_data}\n')
            self.__saved = True

    def find(self, find_str: str) -> list[Contact]:
        find_str = find_str.lower()
        return [contact for contact in self.__pb.values() if find_str in contact]

    def foreach(self, consumer: Callable[[Contact], None], or_else: Callable[[], None] = None):
        if len(self) == 0 and or_else is not None:
            or_else()
        else:
            for contact in self.__pb.values():
                consumer(contact)

    def add(self, base_contact: BaseContact) -> Contact:
        current_id = (max(self.__pb.keys()) if len(self.__pb) != 0 else 0) + 1
        contact = Contact(current_id, base_contact.fio, base_contact.phone, base_contact.comment)
        self.__pb[current_id] = contact
        self.__saved = False
        return contact

    def delete(self, contact_id: int) -> Contact:
        contact = self.__pb.pop(contact_id)
        self.__saved = False
        return contact

    def get(self, contact_id: int) -> Contact:
        return self[contact_id]

    def modify(self, contact_id: int, base_contact: BaseContact):
        self[contact_id] = base_contact

    def open(self, pb_filename: str):
        pb = dict()
        if os.path.exists(pb_filename):
            with open(pb_filename, "r") as input_file:
                for line in input_file:
                    (contact_id, fio, phone, comment) = map(lambda s: s.strip(), line.split(";"))
                    contact_id = int(contact_id)
                    pb[int(contact_id)] = Contact(contact_id, fio, phone, comment)
        self.__pb = pb
        self.__filename = pb_filename
        self.__opened = True
        pass

    def opened(self) -> bool:
        return self.__opened

    def get_contacts(self) -> Iterable[Contact]:
        return self.__pb.values()

    def contains_id(self, contact_id: int) -> bool:
        return contact_id in self

    def is_pb_saved(self) -> bool:
        return self.saved
