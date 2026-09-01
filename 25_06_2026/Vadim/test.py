# l = [1, 9, 10, 15, 67, 70]
# print([i for i in l ])
# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# # b.append(999)
# # print(b)
# # print(a)
# print(list(range(10, 5, -1)))
# # for i in [5, 6, 7, 8, 9]:
# #     print(i)

# l = [5, 10, 15, -4, -8]
# for i in range(len(l) - 1):
#     print(l[i], l[i + 1])
# l = [10, 5, 50, -6, 30, -5]
# print([x ** 2 for x in l if x < 0])
# 5 10 15 20
s = '5 10 15 20'
print(list(map(int, s.split())))
print([int(d) for d in s.split()])
bytes.fromhex('3233').