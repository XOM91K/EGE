# Нахождение всех делителей числа
# def dels(d):
#     dls = []
#     for x in range(1, d + 1):
#         if d % x == 0:
#             dls.append(x)
#     return dls
# print(dels(100_000_000))
# def dels(d):
#     dls = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             dls.append(x)
#             dls.append(d // x)
#     return dls
# print(dels(1_000_000_000_000_000))