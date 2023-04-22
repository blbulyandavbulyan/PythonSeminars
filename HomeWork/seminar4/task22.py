# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во
# элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def read_list_of_integers_from_keyboard(length: int) -> list[int]:
    result = []
    for i in range(length):
        result.append(int(input(f'Введите элемент {i+1}: ')))
    return result


def find_unique_intersection(list_1_: list, list_2_: list) -> list:
    return list(set(list_1_).intersection(set(list_2_)))


list_1_length = int(input('Введите длину первого набора: '))
list_1 = read_list_of_integers_from_keyboard(list_1_length)
list_2_length = int(input('Введите длину второго набора: '))
list_2 = read_list_of_integers_from_keyboard(list_2_length)
result_list = find_unique_intersection(list_1, list_2)
result_list.sort()
print(result_list)
