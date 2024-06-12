import sys
sys.setrecursionlimit(5000)
def F(n):
    if n > 3000:
        return n
    if n <= 3000:
        return F(n + 2) + 2
print(F(40) - F(43))