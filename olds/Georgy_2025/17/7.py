l = [int(x) for x in open("7.txt")]
ct = 0
kr32 = len([x for x in l if x % 32 == 0])
d = []
for x in range(len(l) - 1):
    if l[x] < 0 or l[x + 1] < 0:
        if l[x] + l[x+1] < kr32:
            d.append(l[x] + l[x + 1])
            ct += 1
print(ct,max(d))