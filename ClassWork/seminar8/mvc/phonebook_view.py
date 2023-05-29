from abc import ABCMeta, abstractmethod
from typing import Iterable

from phonebook.contact import Contact, BaseContact


class PhoneBookView:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read_pb_file_name(self, msg: str) -> str: raise NotImplementedError()

    @abstractmethod
    def main_menu(self, main_menu_str: str, valid_choices: range): raise NotImplementedError()

    @abstractmethod
    def print_contacts(self, contacts: Iterable[Contact], message_if_empty: str): raise NotImplementedError()

    @abstractmethod
    def print_message(self, message: str): raise NotImplementedError()

    @abstractmethod
    def read_new_contact(self, input_contact_parts_messages: dict[str, str]) -> Contact: raise NotImplementedError()

    @abstractmethod
    def read_modified_contact(self, contact: BaseContact) -> BaseContact: raise NotImplementedError()

    @abstractmethod
    def ask_yes_no_question_from_user(self, question_msg: str) -> bool: raise NotImplementedError()
