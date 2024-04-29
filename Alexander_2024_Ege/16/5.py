import sys
sys.setrecursionlimit(100000)
def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return F(n - 1) / 3
    if n > 1 and n % 2 != 0:
        return 6 * F(n - 1)
print(F(2049) / F(2046))