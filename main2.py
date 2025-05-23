# # l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\1508_1.txt')]
# # rzn = max(l) - min(l)
# # print(rzn)
# # sm = []
# # for x in range(len(l) - 1):
# #     for y in range(x + 1, len(l)):
# #         k = 0
# #         if len(str(abs(l[x]))) == 5 and l[x] < 0 and l[x] % 46 == 0:
# #             k += 1
# #         if len(str(abs(l[y]))) == 5 and l[y] < 0 and l[y] % 46 == 0:
# #             k += 1
# #         if k == 1:
# #             if abs(l[x] - l[y]) ** 2 % rzn == 0:
# #                 sm.append((l[x] - l[y]) ** 2)
# #                 print(l[x], l[y])
# # print(len(sm), max(sm))
#
# l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\1508_1.txt')]
# sr=  []
# mn102 = min([x for x in l if str(x)[-3:] == '102' and x > 0])
# for x in range(len(l) - 2):
#     for y in range(x + 1, len(l) - 1):
#         for z in range(y + 1, len(l)):
#             k = 0
#             if len(str(abs(l[x]))) == 5 and l[x] > 0 and l[x] % 3 == 0:
#                 k += 1
#             if len(str(abs(l[y]))) == 5 and l[y] > 0 and l[y] % 3 == 0:
#                 k += 1
#             if len(str(abs(l[z]))) == 5 and l[z] > 0 and l[z] % 3 == 0:
#                 k += 1
#             if k == 2:
#                 if (l[x] ** 2 + l[y] ** 2 + l[z] ** 2) % mn102 == 0:
#                     sr.append((l[x] + l[y] + l[z]) / 3)
#                     print(x)
# print(len(sr), int(min(sr)))

# def f(x, y, c, d):
#     if x < y:
#         return 0
#     if x == y and c == 6:
#         print('zzz', y, d)
#         return 1
#     if x == y and c > 6:
#         return 0
#     if x > y:
#         return f(x - 2, y, c + 1, d + '1') + f(x / 3, y, c + 1, d + '2')
# for x in range(100, 1000):
#     for y in range(5, 1000):
#         try:
#             if (f(x, y, 0, '')) == 1:
#                 print(x, y)
#
#         except:
#             pass
tr = [(10, 5, 3), (7, 8, 2), (4, 4, 4), (9, 1, 10), (6, 3, 3), (5, 5, 0), (12, 7, 5), (3, 2, 1), (8, 6, 2), (11, 9, 3), (2, 2, 2), (10, 10, 10)]


for B in range(1, 100):
    c = 0
    for d in tr:
        x = d[0]
        y = d[1]
        z = d[2]
        if (x + y > B and z < 5) or (x - y == z):
            c += 1
    if c == 5:
        print(B)
        break