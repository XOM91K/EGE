# # x = []
# # for N in range(1, 1000):
# #     R = bin(N)[2:]
# #     if N % 3 == 0:
# #         R = R + R[-3:]
# #     else:
# #         R = R + bin((N % 3) * 3)[2:]
# #     R = int(R, 2)
# #     if R > 151:
# #         x.append(R)
# # print(min(x))
# l = []
# def v3(d):
#     s = ''
#     while d > 0:
#         s += str(d % 3)
#         d //= 3
#     return s[::-1]
# for N in range(11, 10000):
#     R = v3(N)
#     if R.count('0') + R.count('2') > R.count('1'):
#         R = '22' + R
#     else:
#         R = '11' + R
#     R = int(R, 3)
#     if R > 100:
#         l.append(R)
# print(min(l))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
d = '121211212212212211'
print(d.count('1') + d.count('2') * 2)