def is_prime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return n > 1
# import fnmatch
# for x in range(2627, 10 ** 9, 2627):
#     if fnmatch.fnmatch(str(x), '7*53?3*1'):
#         print(x, x // 2627)

print(is_prime(2147483647))
