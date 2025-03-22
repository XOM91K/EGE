# def S(n):
#     dls = []
#     for x in range(1, int(n ** 0.5) + 1):
#         if n % x == 0:
#             dls.append(x)
#             dls.append(n // x)
#     return sum(set(dls))
# for x in range(1000, 10000):
#     s = S(x)
#     if str(s)[-2:] == '23':
#         print(x, s)
# import string
# print(string.ascii_uppercase)