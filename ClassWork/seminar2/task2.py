'''Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''


def get_number_of_fibonachi_number(n: int) -> int:
    first_last_number = 0
    second_last_number = 1
    current_fibonachi = 0
    counter = 1
    while (current_fibonachi <= n):
        current_fibonachi = first_last_number + second_last_number
        second_last_number = first_last_number
        first_last_number = current_fibonachi
        # print(current_fibonachi)
        counter += 1
        if (n == current_fibonachi):
            return counter

    return -1


number = int(input('Введите n: '))
print(get_number_of_fibonachi_number(number))
