l = [int(x) for x in open('18.txt')]
ct7 = len([x for x in l if str(x)[-1] == '7'])
mx = []
for x in range(len(l) - 1):
    k = 0
    if l[x] < 0 and l[x + 1] > 0:
        k += 1
    if l[x] > 0 and l[x + 1] < 0:
        k += 1
    if k == 1:
        if l[x] + l[x + 1] < ct7:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))