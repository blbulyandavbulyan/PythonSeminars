# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
def is_number_simple(n:int )->bool:
    if n == 2:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def brute_test(n:int)->bool:
    if n == 2:
        return True
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

for i in range(10000000):
    print(f'Testing number {i}')
    brute = brute_test(i)
    nbrute = is_number_simple(i)
    if brute != nbrute:
        print(f'Test failed on {i}, brute result: {brute}, nbrute result :{nbrute}')
        break
else:
    print('Тест пройден!')