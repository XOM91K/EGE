# # #1 средний балл
# # # n = int(input())
# # # l = []
# # # for x in range(n):
# # #     info = input().split()
# # #     l.append(info)
# # # l = sorted(l, key=lambda d: (-float(d[1]), str(d[0])))
# # # for x in l:
# # #     print(x[1], x[0])
# #
# # # второе задание четные числа
# # # # лямбда-функции (функции в 1 строчку)
# # # l = list(map(int, input().split()))
# # # print([x for x in l if x % 2 == 0])
# #
# #
# # # #проверка числа на простоту
# # # def is_prime(d):
# # #     for x in range(2, int(d ** 0.5) + 1):
# # #         if d % x == 0:
# # #             return False
# # #     return d > 1
# # # print(is_prime(2))
# #
# # s = 'привет Привет ПРИВЕТ как дела ДЕЛА? у меня все хорошо! хорошо.'.lower()
# # for x in '!@#$%^&*()_,./?:':
# #     s = s.replace(x, '')
# # #ответ на 1-й вопрос
# # # s = set(s.split())
# # # print(len(s))
# # #ответ на 2-й вопрос
# # # s = s.split()
# # # new_s = []
# # # for x in s:
# # #     if s.count(x) == 1:
# # #         new_s.append(x)
# # # print(len(new_s))
# # s = 'asdadsa'
# # print(s.islower())
# # def is_ok():
# #     print('ok')
# # def is_neok():
# #     print('neok')
# # is_neok()
# # is_ok()
# # 10
# # Кирилл информатика 5
# # Кирилл физика 5
# # София информатика 4
# # София литература 4
# # София биология 4
# # Лев физика 4
# # Лев математика 3
# # Лев химия 2
# # Ярослав литература 5
# # Яна математика 4
# n = 10
# f = open('1543.txt', encoding='utf-8')
# sl = {}
# for x in range(n):
#     name = f.readline().split()
#     if name[0] not in sl:
#         sl[name[0]] = [0, 0]
#     sl[name[0]][0] += int(name[2])
#     sl[name[0]][1] += 1
# sl = sl.items()
# sl = sorted(sl, key=lambda d: -d[1][0]/d[1][1])
# for x in sl:
#     print(x[1][0] / x[1][1], x[0])
#
# # sl2 = {'one': 1, 2: 222}
# # print(sl2.items())
#1_000_000
#
# def prime_mn(d):
#     ct = 0
#     i = 2
#     while i * i <= d:
#         while d % i == 0:
#             ct += 1
#             d //= i
#         i += 1
#     if d > 1:
#         ct += 1
#     return ct
# #A = int(input())
# A = 1000000
# CT = 0
# for x in range(2, A + 1):
#     CT += prime_mn(x)
# print(CT)
# def sum_dels(d):
#     sm = 0
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             sm += x
#             if x != d // x:
#                 sm += d // x
#     return sm + 1
# k = 1000 # 16    1 2 4 8 16
# for x in range(1, k + 1):
#     for y in range(1, k + 1):
#         smX = sum_dels(x)
#         if smX == y:
#             print(x, y, x - y, x / y)
#
# import itertools
# N = 1000
# for y in range(1, 5):
#     for x in itertools.product('0123456789', repeat=y):
#         sm_pr = 0
#         for z in x:
#             sm_pr += int(z) ** 2
#         if sm_pr == N:
#             print(x)
# 10 ** 2 + 10 ** 2 + 10 ** 2 + 10 ** 2
# [1-9][1-9][1-9][1-9] 9 9 9 9  6561
# N = 1000
# for x in range(0, int(N ** 0.5) + 1):
#     for y in range(1, int(N ** 0.5) + 1):
#         for z in range(1, int(N ** 0.5) + 1):
#             for w in range(1, int(N ** 0.5) + 1):
#                 if x ** 2 + y ** 2 + z ** 2 + w ** 2 == N:
#                     print(f'{x}**2 + {y} ** 2 + {z} ** 2 + {w} ** 2')
# N = int(input())
# if N % 2 == 0:
#     print(0)
# else:
#     for x in range(1, 1000):
#         n = '1' * x
#         if int(n) % N == 0:
#             print(x)
#             break
# for x in range(10):
#     for y in range(10):
#         print('Привет')
#         exit()
# print('ok')
# def longest_common_prefix(s):
#     pr = s[0]
#     for x in range(len(pr)):
#         for y in range(len(s) - 1):
#             if pr[x] != s[y + 1][x]:
#                 return pr[:x]
#     return pr
# print(longest_common_prefix(["flow", "flow", "flow"]))


# yellow yellaw yelcer
# l = ['yell', 'yell', 'yell']
# def longest_common_prefix(l):
#     for x in range(len(l[0])):
#         for y in l:
#             if l[0][:x] != y[:x]:
#                 return y[:x - 1]
#     return l[0]
# a = int(input())
# n = int(input())
# try:
#     print(pow(a, -1, n))
# except:
#     print(0)


