import fnmatch
def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        if is_prime(sum(map(int, str(x)))):
            print(x, x // 2627)
#ЛИНЕЙНАЯ СЛОЖНОСТЬ
# def is_prime(n):
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     return n > 1
#ЛОГАРИФМИЧЕСКАЯ СЛОЖНОСТЬ
# def is_prime(n):
#     for x in range(2, int(n ** 0.5) + 1):
#         if n % x == 0:
#             return False
#     return n > 1
#
# print(is_prime(2147483647))
# 2-3 минуты