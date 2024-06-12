l = [int(x) for x in open('4.txt')]
mn_1 = 10 ** 10
for x in l:
    if str(x)[-1] == '1':
        mn_1 = min(mn_1, x)
pr = []
for x in range(len(l) - 1):
    if str(min(l[x], l[x + 1]))[-1] == '4':
        if l[x] ** 2 + l[x + 1] ** 2 < mn_1 ** 2:
            pr.append(l[x] ** 2 + l[x + 1] ** 2)
print(len(pr), max(pr))