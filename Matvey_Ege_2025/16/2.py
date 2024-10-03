import sys
print(sys.getrecursionlimit())
def F(n):
    if n < 7:
        return 7
    if n >= 7 and n % 3 != 0:
        return 5 - F(n - 1)
    if n >= 7 and n % 3 == 0:
        return 3 + F(n - 1)
print(F(3015))