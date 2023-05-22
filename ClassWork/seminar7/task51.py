# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
#
def same_by(characteristics, *objects) -> bool:
    return len(set(map(characteristics, objects))) <= 1
if __name__ == '__main__':
    print(same_by(lambda x: x % 2 == 0, 2, 2, 6, 4, 8))