import sys
sys.setrecursionlimit(100000)
def F(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return n + F(n + 1) + 1
    if n <= 3000 and n % 2 != 0:
        return F(n + 2) + 2
print(F(40) - F(43))
