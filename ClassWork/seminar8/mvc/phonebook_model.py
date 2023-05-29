from abc import abstractmethod, ABCMeta

from phonebook.contact import BaseContact, Contact


class PhoneBookModel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, bc: BaseContact) -> Contact: raise NotImplementedError()

    @abstractmethod
    def delete(self, contact_id: int) -> Contact: raise NotImplementedError()

    @abstractmethod
    def find(self, str_to_find: str): raise NotImplementedError()

    @abstractmethod
    def save(self): raise NotImplementedError()

    @abstractmethod
    def saved(self) -> bool: raise NotImplementedError()
    @abstractmethod
    def open(self, pb_filename: str): raise NotImplementedError()
