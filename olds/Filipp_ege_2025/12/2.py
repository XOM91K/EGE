# for n in range(4, 1000):
#     s = '2' + '5' * n
#     while '25' in s or '35' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '53', 1)
#         if '35' in s:
#             s = s.replace('35', '2', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)
#     if sum(map(int, s)) % 7 == 0:
#         print(n)
#         break
s = '1231232341244124125'
print(list(map(lambda d: int(d) ** 2, s)))