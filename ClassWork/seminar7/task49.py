# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет
# найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен
# быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в
# два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
#
import random


def generate_sequence_of_orbits(count_of_orbits: int)->list[tuple[int, int]]:
    result = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(count_of_orbits)]
    return result
def find_farthest_orbit(list_of_orbits: list[tuple[int, int]]) -> tuple[int, int]:
    squares = [(i, e[0]*e[1]) for i, e in enumerate(list_of_orbits) if e[0] != e[1]]
    max_square = max(squares, key=lambda x: x[1])
    return list_of_orbits[max_square[0]]

orbits = generate_sequence_of_orbits(10)
print(orbits)
print(find_farthest_orbit(orbits))