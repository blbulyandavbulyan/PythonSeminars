class ContactException(RuntimeError):
    pass

class InvalidContactId(ContactException):  # исключение, бросаемое в случае если в файле есть контакт с ид -1
    pass

class IllegalFIO(ContactException):
    pass
class IllegalComment(ContactException):
    pass
class IllegalPhone(ContactException):
    pass
def get_filtered_string(s: str) -> str:
    return s.replace(";", "").strip()


class BaseContact(object):
    __fio = ""
    __phone = ""
    __comment = ""

    def __init__(self, fio: str, phone: str, comment: str):
        self.fio = fio
        self.phone = phone
        self.comment = comment

    @property
    def fio(self):
        return self.__fio

    @property
    def phone(self):
        return self.__phone

    @property
    def comment(self):
        return self.__comment

    @fio.setter
    def fio(self, new_fio: str):
        if len(new_fio := get_filtered_string(new_fio)) != 0:
            self.__fio = new_fio
        else:
            raise IllegalFIO("Фамилия пуста!")

    @phone.setter
    def phone(self, new_phone: str):
        if len(new_phone := get_filtered_string(new_phone)) != 0:
            self.__phone = new_phone
        else:
            raise IllegalPhone("Телефон пуст!")

    @comment.setter
    def comment(self, new_comment: str):
        if len(new_comment := get_filtered_string(new_comment)) != 0:
            self.__comment = new_comment
        else:
            raise IllegalComment("Комментарий пуст!")


class Contact(BaseContact):
    def __init__(self, contact_id: int, fio: str, phone: str, comment: str):
        super().__init__(fio, phone, comment)
        if contact_id == -1:
            raise InvalidContactId(f"ИД контакта не может быть -1")
        self.__contact_id = contact_id

    def __contains__(self, item: str) -> bool:
        item_cf = item.casefold()
        return item_cf in self.__fio.casefold() or item_cf in self.__phone or item_cf in self.__comment

    def __str__(self):
        return f'Контакт {self.contact_id}\n\tФИО: {self.fio},\n\tТелефон: {self.phone}\n\tКомментарий: {self.comment}'

    @property
    def file_data(self) -> str:
        return f'{self.__contact_id};{self.__fio};{self.__phone};{self.__comment}'

    @property
    def contact_id(self):
        return self.__contact_id
