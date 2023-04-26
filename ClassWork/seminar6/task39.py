# 39. Даны два списка чисел. Требуется вывести те элементы первого списка (в том порядке, в каком они идут в первом
# списке), которых нет во втором массиве
import random

list_1 = [random.randint(0, 10) for _ in range(10)]
list_2 = [random.randint(0, 10) for _ in range(5)]
result_list = [i for i in list_1 if i not in list_2]
print(list_1)
print(list_2)
print(result_list)
