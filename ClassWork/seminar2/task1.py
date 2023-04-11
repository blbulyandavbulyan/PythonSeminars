'''
Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
'''


def factorial(n: int) -> int:
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


number = int(input('Введите число: '))

print(factorial(number))
