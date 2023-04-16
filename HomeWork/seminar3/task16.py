# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

def count_of_x_in_list(x: int, l: list)->int:
    result = 0
    for i in l:
        if x == i:
            result += 1
    return result


number_of_elements = int(input('Введите количество чисел: '))
number_to_count = int(input('Введите число, количество повторений которого нужно найти: '))
random_list = [random.randint(-100, 100) for i in range(number_of_elements)]
print(f'Сгенерированный список: {random_list}')
print(f'Число {number_to_count} встречается в списке {count_of_x_in_list(number_to_count, random_list)}')
