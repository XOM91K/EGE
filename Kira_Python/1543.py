# #1 средний балл
# # n = int(input())
# # l = []
# # for x in range(n):
# #     info = input().split()
# #     l.append(info)
# # l = sorted(l, key=lambda d: (-float(d[1]), str(d[0])))
# # for x in l:
# #     print(x[1], x[0])
#
# # второе задание четные числа
# # # лямбда-функции (функции в 1 строчку)
# # l = list(map(int, input().split()))
# # print([x for x in l if x % 2 == 0])
#
#
# # #проверка числа на простоту
# # def is_prime(d):
# #     for x in range(2, int(d ** 0.5) + 1):
# #         if d % x == 0:
# #             return False
# #     return d > 1
# # print(is_prime(2))
#
# s = 'привет Привет ПРИВЕТ как дела ДЕЛА? у меня все хорошо! хорошо.'.lower()
# for x in '!@#$%^&*()_,./?:':
#     s = s.replace(x, '')
# #ответ на 1-й вопрос
# # s = set(s.split())
# # print(len(s))
# #ответ на 2-й вопрос
# # s = s.split()
# # new_s = []
# # for x in s:
# #     if s.count(x) == 1:
# #         new_s.append(x)
# # print(len(new_s))
# s = 'asdadsa'
# print(s.islower())
def is_ok():
    print('ok')
def is_neok():
    print('neok')
is_neok()
is_ok()