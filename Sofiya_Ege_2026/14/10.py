# def f15(n):
#     s = []
#     while n > 0:
#         s.append(n % 15)
#         n //= 15
#     return s[::-1]
#
#
# for x in range(11, 10 ** 6, 11):
#     a = 15 ** 450 + 15 ** 100 - 11123471 - x
#     a = f15(a)
#     if a.count(14) == 97:
#         print(x)
# s = [1, 2, 3]
# print(s.count('hello'))