from typing import Callable, Iterable

import text
from mvc.phonebook_view import PhoneBookView
from phonebook.contact import BaseContact, Contact


def read_not_empty_str(msg: str) -> str:
    while True:
        result = input(msg).strip()
        if result:
            return result


class PhoneBookConsoleView(PhoneBookView):
    def read_pb_file_name(self, msg: str) -> str:
        file_name = input(msg).strip()
        if not file_name:
            file_name = "contacts.txt"
        return file_name

    def main_menu(self, main_menu_str: str, valid_choices: range):
        print(main_menu_str)
        while True:
            try:
                your_choice = int(input(text.enter_your_choice))
                if your_choice in valid_choices:
                    return your_choice
            except ValueError:
                self.print_error(text.you_enter_not_a_integer_number)

    def print_contacts(self, contacts: Iterable[Contact], message_if_empty: str):
        for contact in contacts:
            print(f'* {contact.contact_id:>3} | {contact.fio:^30} | {contact.phone:>30} | {contact.comment:>15} *')

    def print_message(self, message: str):
        print('\n' + '=' * (len(message) + 2))
        print('*' + message + '*')
        print('\n' + '=' * (len(message) + 2))

    def print_error(self, error: str):
        print('\n' + '=' * (len(error) + 2))
        print('*' + error + '*')
        print('=' * (len(error) + 2))

    def read_new_contact(self, input_contact_parts_messages: dict[str, str]) -> BaseContact:
        fio = read_not_empty_str(input_contact_parts_messages['fio'])
        phone = read_not_empty_str(input_contact_parts_messages['phone'])
        comment = read_not_empty_str(input_contact_parts_messages['comment'])
        return BaseContact(fio, phone, comment)

    def read_search_line(self, msg: str) -> str:
        return input(msg)

    def read_modified_contact(self, contact: BaseContact, input_contact_parts_messages: dict[str, str]) -> BaseContact:
        print(text.leave_blank_to_not_change)
        fio = input(input_contact_parts_messages['fio']).strip()
        if not fio:
            fio = contact.fio
        phone = input(input_contact_parts_messages['phone']).strip()
        if not phone:
            phone = contact.phone
        comment = input(input_contact_parts_messages['comment']).strip()
        if not comment:
            comment = contact.comment
        return BaseContact(fio, phone, comment)

    def ask_yes_no_question_from_user(self, question_msg: str) -> bool:
        answer = read_not_empty_str(question_msg).lower()
        if answer == 'y':
            return True
        else:
            return False

    def read_contact_id(self, message: str, is_contact_id_valid: Callable[[int], bool]) -> int:
        while True:
            try:
                contact_id = int(read_not_empty_str(message))
                if contact_id != -1 and not is_contact_id_valid(contact_id):
                    self.print_error(text.phonebook_does_not_contain_given_contact_id)
                else:
                    return contact_id
            except ValueError:
                self.print_error(text.you_enter_not_a_integer_number)
                continue
