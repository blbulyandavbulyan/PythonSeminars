'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
# моё любимое, сейчас я как возьму и использую функцию из предыдущей задачи, где мы считали сумму цифр
from task1 import find_summ_of_digits


def is_ticket_number_contains_six_digits(ticket_number: int):
    return ticket_number // 100000 > 1


def is_ticket_happy(ticket_number: int):
    if not is_ticket_number_contains_six_digits(ticket_number):
        return False
    first_three_digits = ticket_number // 1000
    second_three_digits = ticket_number - first_three_digits * 1000
    return find_summ_of_digits(first_three_digits) == find_summ_of_digits(second_three_digits)


ticket_number = int(input('Введите номер билета: '))
print('yes' if is_ticket_happy(ticket_number) else 'no')
