# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def recursive_power(base_: float, power_: int) -> float:
    if power_ == 0:
        return 1
    else:
        return base_*recursive_power(base_, power_ - 1)


base = float(input('Введите основание: '))
power = int(input('Введите степень: '))
print(f'{base} в степени {power} = {recursive_power(base, power)}')