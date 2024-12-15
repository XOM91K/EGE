#https://examinf.ru/tasks/17
l = [int(x) for x in open('1.txt')]
sr = sum(l) / len(l)
ct = 0
d = []
for x in range(len(l) - 1):
    if l[x] < sr or l[x + 1] < sr:
        if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x + 1] % 7 == 0 and l[x + 1] % 3 != 0 and l[x + 1] % 11 != 0 and l[x + 1] % 13 != 0):
            d.append(l[x] + l[x + 1])
            ct += 1
print(ct)
print(min(d))
# for x in l:
#     print(x, x + 1)
# print(sr)
# print(l)