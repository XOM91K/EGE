l = [int(x) for x in open('15.txt')]
kr32 = len([x for x in l if x % 32 == 0])
mx = []
for x in range(len(l) - 1):
    if l[x] < 0 or l[x + 1] < 0:
        if l[x] + l[x + 1] < kr32:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))