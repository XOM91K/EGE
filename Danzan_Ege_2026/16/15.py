# import sys, functools
# sys.setrecursionlimit(1000000)
# @functools.lru_cache(None)
# def F(n):
#     if n < 10:
#         return 3
#     if n >= 10:
#         return (n + 4) * F(n - 5)
# for x in range(1, 260_000):
#     F(x)
# print((F(257487) / 683 + F(257477) / 67) / F(257472))
n = [3] * 10
for x in range(10, 287500):
    n.append((x + 4) * n[x - 5])
