import sys, functools
sys.setrecursionlimit(100_000)
@functools.lru_cache(None)
def F(n):
    if n > 2024:
        return 2
    if n == 2024:
        return 1
    if n < 2024:
        return n * (n + 1) + F(n + 1) - F(n + 2)
for x in range(5000, 1, -1):
    F(x)
print(F(100) - F(10) + F(2020))

#1-й этап мы просто переписываем код и запускаем
#если видим ошибку "maximum recursion depth exceeded in comparison" то 2-й этап вызываем библиотеку
#import sys и setrecursionlimit 100_000
#если долго выводится, либо не выводится ответ, то 3-й этап
#import functools , @functools.lru_cache(None)
#если ошибка "Process finished with exit code -1073741571 (0xC00000FD)"
#то 4-й этап:
#for x in range(5000, 1, -1):
#    F(x)