#функция проверки на простоту
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1

print(is_prime(0))

#n = 1000
# def dels(d):
#     dls = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             dls.append(x)
#             dls.append(d // x)
#     return sorted(set(dls))
# print(dels(n))