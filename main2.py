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
# tr = [(10, 5, 3), (7, 8, 2), (4, 4, 4), (9, 1, 10), (6, 3, 3), (5, 5, 0), (12, 7, 5), (3, 2, 1), (8, 6, 2), (11, 9, 3), (2, 2, 2), (10, 10, 10)]
#
#
# for B in range(1, 100):
#     c = 0
#     for d in tr:
#         x = d[0]
#         y = d[1]
#         z = d[2]
#         if (x + y > B and z < 5) or (x - y == z):
#             c += 1
#     if c == 5:
#         print(B)
#         break
# def v11(n):
#     s = []
#     while n > 0:
#         s.append(n % 15)
#         n //= 15
#     return s[::-1]
# for x in range(1, 100000):
#     d = 15 ** 450 + 15 ** 100 - 11123471 - x
#     d = v11(d)
#     if d.count(14) == 97:
#         print(x % 11, x, d.count(14))

# l = [[int(d) for d in x.split()] for x in open('main2.txt')]
# k = 0
# for x in l:
#     k += 1
#     if sorted(x) == x:
#         povt4 = [y for y in x if x.count(y) == 4]
#         povt2 = [y for y in x if x.count(y) == 2]
#         povt1 = [y for y in x if x.count(y) == 1]
#         if len(povt4) == 4 and len(povt2) == 2 and len(povt1) == 1:
#             if k % 7 == 0:
#                 if max(povt4 + povt2) <= povt1[0]:
#                     print(k, x)

# l = [[int(d) for d in x.split()] for x in open('main2.txt')]
# sm = 0
# for x in l:
#     k = 0
#     if sorted(x)[::-1] == x:
#         k += 1
#     povt3 = [y for y in x if x.count(y) == 3]
#     povt2 = [y for y in x if x.count(y) == 2]
#     povt1 = [y for y in x if x.count(y) == 1]
#     if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 1:
#         k += 1
#     if len(povt3) + len(povt2) > 0 and len(povt1) > 0 and min(povt3 + povt2) > povt1[0]:
#         k += 1
#     if k == 2:
#         print(x)
#         sm += sum(x)
# print(sm)
l = [int(x) for x in open('main2.txt')]
mx = []
mn21 = min([x for x in l if x > 0 and len(str(abs(x))) == 4 and sum(map(int, str(x))) == 21])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and sum(map(int, str(abs(l[x])))) == 15:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and sum(map(int, str(abs(l[x + 1])))) == 15:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and sum(map(int, str(abs(l[x + 2])))) == 15:
        k += 1
    if k == 2:
        if (l[x] + l[x + 1] + l[x + 2]) * 98 >= mn21 ** 2:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))