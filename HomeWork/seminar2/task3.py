'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
N = int(input('Введите N: '))
current = 1
power_counter = 1
while current < N:
    print(current)
    current = current << 1 # тут я решил использовать операцию побитового сдвига

