l = [int(x) for x in open('5.txt')]
mx = []
q = len([y for y in l if str(y)[-1] == '7'])
for x in range(len(l) - 1):
    if (l[x] < 0 and l[x + 1] > 0) or (l[x] > 0 and l[x + 1] < 0):
        if l[x] + l[x + 1] < q:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))