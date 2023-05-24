# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
# Поля: ФИО, телефон, комментарий
from textwrap import dedent

from phonebook.phonebook import PhoneBook
from phonebook.contact import BaseContact


def load_pb_from_typed_filename() -> PhoneBook:
    filename = input('Введите имя файла с контактами(оставьте пустым для варианта по умолчанию): ')
    if len(filename) == 0:
        filename = "contacts.txt"
    return PhoneBook(filename)


def read_contact_id(pb: PhoneBook, message: str) -> int:
    while (contact_id := int(input(f'Введите ИД для {message} или -1 для отмены: '))) not in pb and contact_id != -1:
        print('Такого ИД нет в справочнике, повторите попытку!')
    else:
        return contact_id


def modify_contact(pb: PhoneBook, contact_id: int) -> None:
    print('Выберите что вы хотите изменить?\n\t1)ФИО\n\t2)Телефон\n\t3)Комментарий')
    contact = pb[contact_id]
    fio = contact.fio
    phone = contact.phone
    comment = contact.comment
    variants = input()
    for variant in variants:
        match variant:
            case '1':
                fio = input('Введите новое ФИО: ')
            case '2':
                phone = input('Введите новый телефон: ')
            case '3':
                comment = input('Введите новый комментарий: ')
    pb[contact_id] = BaseContact(fio, phone, comment)


def read_contact() -> BaseContact:
    fio = input('Введите ФИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return BaseContact(fio, phone, comment)


def ask_user_for_save_pb(pb: PhoneBook):
    save_or_not = ""
    while True and not pb.saved:
        save_or_not = input('Вы не сохранили уже открытый справочник хотите сохранить ?(y/n): ')
        if save_or_not == 'y':
            pb.save()
            break
        if save_or_not == 'n':
            break


if __name__ == '__main__':
    stopped = False
    pb = load_pb_from_typed_filename()
    while not stopped:
        print(dedent("""
                        1. Открывать другой файл
                        2. Сохранить файл
                        3. Показать все контакты
                        4. Добавить контакт
                        5. Найти контакт
                        6. Изменить контакт
                        7. Удалить контакт
                        8. Выход
                    """))
        match input('Введите действие: '):
            case '1':
                ask_user_for_save_pb(pb)
                pb = load_pb_from_typed_filename()
            case '2':  # Сохранение
                pb.save()
            case '3':  # распечатка
                pb.foreach(print, lambda: print('Список контактов пуст!'))
            case '4':
                new_contact = read_contact()
                pb.add(new_contact)
            case '5':
                found_contacts = pb.find(input('Введите подстроку для поиска: '))
                for found_contact in found_contacts:
                    print(found_contact)
                if len(found_contacts) == 0:
                    print('По вашему запросу контакты не найдены')
            case '6':
                contact_id_for_modify = read_contact_id(pb, "изменения")
                if contact_id_for_modify != -1:
                    if contact_id_for_modify in pb:
                        modify_contact(pb, contact_id_for_modify)
                    else:
                        print('Контакта с таким ИД в справочнике нет')
            case '7':
                contact_id_for_delete = read_contact_id(pb, "удаления")
                if contact_id_for_delete != -1:
                    pb.delete(contact_id_for_delete)
            case '8':
                stopped = True
                ask_user_for_save_pb(pb)
            # pb_core.delete_contact(phonebook, )
