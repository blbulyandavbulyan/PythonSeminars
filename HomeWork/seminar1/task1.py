'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

from math import fabs
def find_summ_of_digits(number: int):
    result = 0
    i = int(fabs(number))
    while (i >= 1):
        result += i % 10
        i = i//10
    return result

if __name__ == "__main__":
    number = int(input('Введите число: '))
    print(f'Сумма цифр числа {number}: {find_summ_of_digits(number)}')