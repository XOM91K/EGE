import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 != 0:
        return n
    if n > 3 and n % 2 == 0:
        return F(n - 1) + F(n - 2) + F(n - 3)
print(F(2254) - F(2252))