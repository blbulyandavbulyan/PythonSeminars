'''

Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''


def check(m: int, n: int, k: int) -> bool:
    return k % m == 0 or k % n == 0


n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k: '))
print('yes' if check(m, n, k) else 'no')
