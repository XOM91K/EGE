import sys
sys.setrecursionlimit(100000)
def F(n):
    if n < 3:
        return 1
    if n > 2:
        return 2*n - 1 + F(n-2)
print(F(3033))