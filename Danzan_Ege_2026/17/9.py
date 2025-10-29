l = [int(x) for x in open('9.txt')]
col7 = len([x for x in l if str(x)[-1] == '7'])
mx = []
for x in range(len(l) - 1):
    if (l[x] > 0 and l[x + 1] < 0) or (l[x] < 0 and l[x + 1] > 0):
            if l[x] + l[x + 1] < col7:
                mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))