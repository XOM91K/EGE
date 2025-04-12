#ахождение всех делителей числа
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


# 12074
# def dels(n):
#     dls = []
#     for x in range(1, int(n ** 0.5) + 1):
#         if n % x == 0:
#             if x % 2 == 0:
#                 dls.append(x)
#             if (n // x) % 2 == 0:
#                 dls.append(n // x)
#     return dls
# print(dels(100))

#Вернуть сумму макс. и мин. делителя числа, кроме едиинцы и самого числа
# 100
# def dels(n):
#     dls = []
#     for x in range(1, int(n ** 0.5) + 1):
#         if n % x == 0:
#             dls.append(x)
#             dls.append(n // x)
#     mxmn = sorted(set(dls))
#     mxmn = mxmn[1] + mxmn[-2]
#     return mxmn
# print(dels(100))