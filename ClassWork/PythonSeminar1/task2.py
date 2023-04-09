'''
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
 Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
'''
finalCount = 0
for i in range(0, 3):
    countStudents = int(input(f'Введите количество учеников в {i + 1}: '))
    count = (countStudents + 1)//2 # формула не моя
    finalCount += count
    print(f'Нужно парт на {i + 1} класс: {count}')
print(f'Всего нужно парт для всех 3 классов: {finalCount}')