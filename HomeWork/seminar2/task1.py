'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
 Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random
count_of_coins = int(input('Введите количество монет: '))
coin_side_names = {0: 'решка', 1: 'герб'}
coins_list = [random.randint(0, 1) for i in range(count_of_coins)] # генерируем список со случайными целыми списками, 0 - решка, 1 - орёл
test = [1, 2 , 3]
coins_list_with_names = [coin_side_names[coin_side_number] for coin_side_number in coins_list] # возможно это и не обязательно было делать, но я решил это тут оставить для более удобного вывода
print(coins_list_with_names)
count_of_heads = count_of_tails = 0

for coin in coins_list:
    if coin == 1:
        count_of_heads+=1
    else:
        count_of_tails+=1

print(f'Минимальное число монет для переворачивания: {min(count_of_tails, count_of_heads)}')