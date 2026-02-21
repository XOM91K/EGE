# # l = '1 2 3 2 4 5 3'
# # l = list(map(int, l.split()))
# # l.pop(-1)
# # l = [x for x in l if l.count(x) == 1]
# # print(*sorted(l))
# l1 = '1 2 3 4'
# l2 = '3 4 5 6'
# l1 = list(map(int, l1.split()))
# l2 = list(map(int, l2.split()))
# l1.append(0)
# print(*sorted(set(l1).intersection(l2))[::-1])

# l = [10, 1, 222, 3, 4, 5]
# n = 5
# for x in range(len(l)):
#     print(l[x])