# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from math import fabs
import random


def find_close_element_to_x_in_list(x: int, l: list) -> int:
    minimum_delta = abs(x - l[0])
    result = l[0]
    for i in range(1, len(l)):
        current_delta = abs(x - l[i])
        if current_delta < minimum_delta:
            minimum_delta = current_delta
            result = l[i]
    return result


count_of_numbers_to_generate = int(input('Введите количество чисел: '))
x = int(input('Введите x: '))
random_list = [random.randint(-100, 100) for i in range(count_of_numbers_to_generate)]
print(f'Сгенерированный список: {random_list}')
print(f'Наиболее близкое к {x} число в списке: {find_close_element_to_x_in_list(x, random_list)}')