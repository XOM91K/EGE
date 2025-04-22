l = [int(x) for x in open('7.txt')]
mn2 = min([y for y in l if len(str(abs(y))) == 2]) ** 2
mx4 = max([y for y in l if str(y)[-1] == '1' and len(str(abs(y))) == 4])
mx = []
for x in range(len(l) - 2):
    k = 0
    if l[x] > mn2:
        k += 1
    if l[x + 1] > mn2:
        k += 1
    if l[x + 2] > mn2:
        k += 1
    if k == 2:
        if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % mx4 == 0:
            mx.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(mx), max(mx))
