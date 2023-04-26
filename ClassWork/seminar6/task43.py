# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
#todo сравнить эту задачу с решением на семинаре
import random

input_list = [random.randint(0, 4) for _ in range(10)]
count_dicts = dict()
for i in input_list:
    if i in count_dicts:
        count_dicts[i] += 1
    else:
        count_dicts[i] = 1
pairs_count = sum(count_dicts.values())
pairs_count //= 2
print(input_list)
print(pairs_count)
