# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи
def fibonaci(n: int) -> int:
    if n in [0, 1]:
        return n
    return fibonaci(n - 2) + fibonaci(n - 1)


print(fibonaci(7))
