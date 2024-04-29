import sys
sys.setrecursionlimit(100000)
def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + F(n / 2 - 1)
    if n > 1 and n % 2 != 0:
        return n + F(n + 2)
    print(n)
print(F(126))
    # if F(n) == 19:
    #     print(n)