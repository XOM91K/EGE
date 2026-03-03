# import functools
# @functools.lru_cache(None)
# def f(x, y, ct):
#     if x > y or x == 10 or x == 38:
#         return 0
#     if x == y:
#         return 1
#     if x < y:
#         return f(x + 1, y, ct + 1) + f(x + 2, y, ct) + f(x * 3, y, ct)
# print(f(1, 43, 0) - )