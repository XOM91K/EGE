# l=[x for x in open('1752.txt')]
# yach=[[int(d) for d in x.split()]for x in l[:200]]
# yach=sorted(yach, key=lambda d: (d[-1], d[0]))
# print(len(yach))
# print(yach)
# for x in yach:
#     x.extend([0, 0, 0])
# print(yach)
# #номер цена занято
# tovar=[[int(d)for d in x.split()]for x in l[200:]]
# tovar = sorted(tovar, key=lambda d: (d[0], d[1]))
# print(tovar)
# #нач кон
# for x in tovar:
#     for y in range(len(yach)):
#             if x[0] > yach[y][-1]:
#                 yach[y][-1] = x[1]
#                 yach[y][2] += (yach[y][1]*(x[-1]-x[0]+1))
#                 yach[y][3] += 1
#                 break
# print(sorted(yach, key=lambda d: (d[2]))[::-1][0][0])
# print(max(yach, key=lambda d: d[-2])[-2])
# nums = [
#     [int(i) for i in x.split()] for x in open(r"1752.txt")
# ]
#
# n, k = nums[0]
# nums = nums[1:]
# boxes = nums[:n]
# data = nums[n:]
# data.sort()
#
# boxes = [[num, cost, [[-1, -1]]] for num, cost in boxes]
#
# for start, end in data:
#     boxes.sort(key=lambda d: (-(d[2][-1][1] < start), d[1], d[0]))
#     if boxes[0][2][-1][1] < start:
#         boxes[0][2].append([start, end])
#
# boxes = [
#     [
#         num,
#         cost,
#         len(queue) - 1,
#         sum([end - start + 1 for start, end in queue[1:]]) * cost,
#     ]
#     for num, cost, queue in boxes
# ]
# print(sorted(boxes, key=lambda d: (-d[-1], -d[0]))[0][0], max([x[2] for x in boxes]))

#1 30
#1 8
#1 16

# =====>



#1 8
# 1 16
# 1 30