def prime(n): #ПРОВЕРКА НА ПРОСТОТУ
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
print(prime(1238123263819363982361393612))
# import fnmatch
# for x in range(2627, 10 ** 9, 2627):
#     if fnmatch.fnmatch(str(x), '7*53?3*1'):
#         if prime(sum(map(int, str(x)))):
#             print(x, x // 2627)