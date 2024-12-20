import fnmatch
def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
# print(is_prime(2147483649))
# for x in range(10 ** 7):
#     if fnmatch.fnmatch(str(x), "3?1111*") and is_prime(x):
#         print(x)