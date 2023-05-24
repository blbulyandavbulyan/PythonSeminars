class InvalidContactId(RuntimeError):  # исключение, бросаемое в случае если в файле есть контакт с ид -1
    pass


class Contact(object):
    def __init__(self, contact_id: int, fio: str, phone: str, comment: str):
        if contact_id == -1:
            raise InvalidContactId(f"ИД контакта не может быть -1")
        self.__contact_id = contact_id
        self.__fio = fio.replace(";", "")
        self.__phone = phone.replace(";", "")
        self.__comment = comment.replace(";", "")

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

    @property
    def fio(self):
        return self.__fio

    @property
    def phone(self):
        return self.__phone

    @property
    def comment(self):
        return self.__comment
