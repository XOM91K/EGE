l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        x.sort()
        if (x[-1] + x[0]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)
# print([x for x in range(1, 1000)])
# d = []
# for x in range(1, 1000):
#     d.append(x)
# print(d)
# print([x for x in range(1, 1000)])