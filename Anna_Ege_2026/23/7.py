# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return d > 0
def obw_dels(d, n):
    for x in range(2, min(d, n)):
        if d % x == 0 and n % x == 0:
            return False
    return True
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if obw_dels(x, x + 1) and obw_dels(x, x + 3) and obw_dels(x, x + 7):
            return f(x + 1, y) + f(x + 3, y) + f(x + 7, y)
        elif obw_dels(x, x + 1) and obw_dels(x, x + 3):
            return f(x + 1, y) + f(x + 3, y)
        elif obw_dels(x, x + 3) and obw_dels(x, x + 7):
            return f(x + 3, y) + f(x + 7, y)
        elif obw_dels(x, x + 1) and obw_dels(x, x + 7):
            return f(x + 1, y) + f(x + 7, y)
        elif obw_dels(x, x + 1):
            return f(x + 1, y)
        elif obw_dels(x, x + 3):
            return f(x + 3, y)
        elif obw_dels(x, x + 7):
            return f(x + 7, y)

# 13, 17, 19, 23, 29, 31
print(f(13, 31))
# 25