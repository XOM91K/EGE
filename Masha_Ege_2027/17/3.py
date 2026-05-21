l = [int(x) for x in open('3.txt')]
ln7 = len([y for y in l if str(y)[-1] == '7'])
mx = []
for x in range(len(l) - 1):
    if (l[x] * l[x + 1]) < 0:
        if l[x] + l[x + 1] < ln7:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))