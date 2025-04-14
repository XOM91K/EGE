# # n = 4
# # # l = [1, 2, 3, 4]
# # def factor(n):
# #     if n == 1:
# #         return 1
# #     return n * factor(n - 1)
# # print(factor(4))
# # 1, 1, 2, 3, 5, 8, 13...
# # def fibo(n):
# #     if n == 1 or n == 2:
# #         return 1
# #     return fibo(n - 1) + fibo(n - 2)
# # print(fibo(20))
#
# d = 100
# def dels(n):
#     dls = []
#     for x in range(1, int(n ** 0.5) + 1):
#         if n % x == 0:
#             dls.append(x)
#             dls.append(n // x)
#     return sorted(set(dls))
# print(dels(d))
print([x for x in range(1, 100)])