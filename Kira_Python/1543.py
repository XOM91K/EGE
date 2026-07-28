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
# def is_ok():
#     print('ok')
# def is_neok():
#     print('neok')
# is_neok()
# is_ok()
# 10
# Кирилл информатика 5
# Кирилл физика 5
# София информатика 4
# София литература 4
# София биология 4
# Лев физика 4
# Лев математика 3
# Лев химия 2
# Ярослав литература 5
# Яна математика 4
n = 10
f = open('1543.txt', encoding='utf-8')
sl = {}
for x in range(n):
    name = f.readline().split()
    if name[0] not in sl:
        sl[name[0]] = [0, 0]
    sl[name[0]][0] += int(name[2])
    sl[name[0]][1] += 1
sl = sl.items()
sl = sorted(sl, key=lambda d: -d[1][0]/d[1][1])
for x in sl:
    print(x[1][0] / x[1][1], x[0])

# sl2 = {'one': 1, 2: 222}
# print(sl2.items())