# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти
# кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

def generate_list_of_counts_of_berries(n: int, a: float) -> list[int]:
    return


number_of_bushes = int(input('Введите количество кустов: '))  # это ничто иное как наше n в задаче
yield_factor = float(input('Введите коэффициент урожайности: '))  # это та самая a, которая умножается на i
list_of_counts_of_berries = [int(yield_factor * i) for i in range(number_of_bushes)]  # наш список с количеством ягод на каждом кусте

maximum_count_of_berries = 0
index_of_middle_element_giving_maximum_summ_of_berries = 0
for i in range(len(list_of_counts_of_berries)):
    count_of_berries_on_left = list_of_counts_of_berries[i]  # количество ягод на левом кусте
    # здесь мы берём остаток от деления на длину списка с количеством ягод на кустах, чтобы закольцевать его
    count_of_berries_in_the_middle = list_of_counts_of_berries[(i + 1) % len(list_of_counts_of_berries)]  # количество ягод на среднем кусте
    count_of_berries_on_right = list_of_counts_of_berries[(i + 2) % len(list_of_counts_of_berries)]  # количество ягод на правом кусте

    current_count_of_berries = count_of_berries_on_left + count_of_berries_in_the_middle + count_of_berries_on_right
    if current_count_of_berries > maximum_count_of_berries:
        maximum_count_of_berries = current_count_of_berries
        index_of_middle_element_giving_maximum_summ_of_berries = count_of_berries_on_right
print(f'Список с ягодами: {list_of_counts_of_berries}')
print(
    f'Максимальное число ягод для сбора за один заход: {maximum_count_of_berries}\n индекс среднего куста: {index_of_middle_element_giving_maximum_summ_of_berries}')
