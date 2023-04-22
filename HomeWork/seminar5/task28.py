# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех
# арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

# Идея в том чтобы увеличить на 1 число first_number столько раз, сколько в числе second_number
# а для того чтобы сумма не изменилась, нужно second_number уменьшить на столько раз, сколько в second_number
def recursive_sum(first_number: int, second_number: int) -> int:
    if first_number == 0 or second_number == 0:
        return first_number if first_number > second_number else second_number
    else:
        return recursive_sum(first_number + 1, second_number - 1)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(recursive_sum(a, b))
