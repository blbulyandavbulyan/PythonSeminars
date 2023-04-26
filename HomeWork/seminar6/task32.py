# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
import random
minimum = int(input('Введите нижнюю границу: '))
maximum = int(input('Введите верхнюю границу: '))
random_list = [random.randint(0, 100) for _ in range(20)]
indexes_of_elements_between_min_and_max = [i for i in range(len(random_list)) if minimum <= random_list[i] <= maximum]
print(random_list)
print(indexes_of_elements_between_min_and_max)
