#
l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        x.sort()
        if (x[0] + x[-1]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)

# l = [5, 10, 15, 20, 25, 30, 35, 40]
# print(l)
# print(l[len(l) // 2])
# l = [x for x in range(5, 1001) if x % 5 == 0] #генератор списков
# print(l)
# l = []
# for x in range(5, 1001):
#     if x % 5 == 0:
#         l.append(x)
# print(l)