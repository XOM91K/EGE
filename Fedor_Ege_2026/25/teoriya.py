# def dels(d):
#     dls = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             dls.append(x)
#             dls.append(d // x)
#     return sorted(set(dls))
# d = 100
# print(dels(d))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
print(is_prime(8))
# print(is_prime(23))
# print(is_prime(43))
# print(is_prime(59))
# print(is_prime(108))
# print(is_prime(12893128361281927))

