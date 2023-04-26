# 41. Дан список, состоящий из целых чисел. Напишите программу, которая в данном списке определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
import random

input_list = [random.randint(0, 20) for _ in range(10)]
result_count = 0
for i in range(1, len(input_list) - 1):
    if input_list[i - 1] < input_list[i] and input_list[i + 1] < input_list[i]:
        result_count += 1
print(input_list)
print(result_count)