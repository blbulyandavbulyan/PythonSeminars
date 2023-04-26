# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число
# вводится с новой строки.

def generate_aripmetic_progression(first_element: int, difference: int, length: int) -> list:
    return [first_element + i * difference for i in
            range(length)]  # формула немного изменена т.к. мы начинаем перебор с 0


a1 = int(input('Введите первый элемент арифм. прогрессии: '))
d = int(input('Введите разность арифм. прогрессии: '))
count_of_elements = int(input('Введите количество элементов: '))
print(generate_aripmetic_progression(a1, d, count_of_elements))