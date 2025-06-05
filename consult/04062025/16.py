import sys

sys.setrecursionlimit(100000)


def F(n):
    if n > 10000:
        return n + 4
    if n <= 10000:
        return 3 * n + 5 + F(n + 3)


print(F(707) - F(716))
l = open('‪C:\Users\Zarif\Downloads\1548_1.txt').readlines()
print(l)

