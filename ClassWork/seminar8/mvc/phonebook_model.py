from abc import abstractmethod, ABCMeta
from typing import Iterable

from phonebook.contact import BaseContact, Contact


class PhoneBookModel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, bc: BaseContact) -> Contact: raise NotImplementedError()

    @abstractmethod
    def modify(self, contact_id: int, base_contact: BaseContact): raise NotImplementedError()

    @abstractmethod
    def delete(self, contact_id: int) -> Contact: raise NotImplementedError()

    @abstractmethod
    def find(self, find_str: str) -> list[Contact]: raise NotImplementedError()

    @abstractmethod
    def save(self): raise NotImplementedError()

    @abstractmethod
    def saved(self) -> bool: raise NotImplementedError()

    @abstractmethod
    def open(self, pb_filename: str): raise NotImplementedError()

    @abstractmethod
    def opened(self) -> bool: raise NotImplementedError()

    @abstractmethod
    def get_contacts(self) -> Iterable[Contact]: raise NotImplementedError()

    @abstractmethod
    def contains_id(self, contact_id: int) -> bool: raise NotImplementedError()
