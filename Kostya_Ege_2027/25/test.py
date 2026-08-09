import tqdm
# d = 100_000_000
# dls = []
# for x in tqdm.tqdm(range(1, d // 2 + 1)):
#     if d % x == 0:
#         dls.append(x)
# dls.append(d)
# print(dls)
# d = 16
# def dels(n):
#     dls = []
#     for x in range(2, int(n ** 0.5) + 1):
#         if n % x == 0:
#             dls.append(x)
#             dls.append(n // x)
#     return sorted(set(dls))
# print(dels(d))
d = 17
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
print(is_prime(17))
