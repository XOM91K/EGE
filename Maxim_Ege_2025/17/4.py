l = [int(x) for x in open('4.txt')]
ct = 0
sr = sum(l)/len(l)
ma = []
for x in range(len(l)-1):
    if l[x] > sr and l[x + 1] > sr:
        if str((l[x] + l[x+1]))[-2:] == '31':
            ct += 1
            ma.append(l[x]+l[x+1])
print(ct, max(ma))