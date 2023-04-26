# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k
# выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно
# натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел,
# каждое из которых не превосходит k.
def find_diveders(number: int)->list:
    return [i for i in range(1, number//2 + 1) if number % i == 0]
# checked_set = set()
for i in range(1, 10000):
    sum_i_diveders = sum(find_diveders(i))
    for j in range(i+1, 10000):
        if j == sum_i_diveders and i == sum(find_diveders(j)):
            print(f'{i} {j}')