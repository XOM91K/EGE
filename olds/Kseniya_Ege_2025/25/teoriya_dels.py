# def dels(n):
#     dls = []
#     for x in range(1, n + 1):
#         if n % x == 0:
#             dls.append(x)
#     return dls
# d = 100_000_000
# print(dels(d))
def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
# 20  [1, 20, 2, 10, 4, 5]
# 1, 2, 4, 5, 10, 20
d = 100
print(dels(d))