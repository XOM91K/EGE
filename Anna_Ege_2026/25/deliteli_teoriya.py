# def dels(n: int) -> list:
#     dls = []
#     for x in range(1, n + 1):
#         if n % x == 0:
#             dls.append(x)
#     return dls
# d = 1_000_000_000
# print(dels(d))
# #2-й способ побыстрее
# def dels(n: int) -> list:
#     dls = []
#     for x in range(1, n // 2 + 1):
#         if n % x == 0:
#             dls.append(x)
#     dls.append(n)
#     return dls
# d = 1_000_000_000
# print(dels(d))
#3-й способ самый быстрый
def dels(n: int) -> list:
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))


d = 100
print(dels(d))