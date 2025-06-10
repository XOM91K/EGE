l = [int(x) for x in open('5.txt')]
sr = sum(l) / len(l)
ct = 0
d = []
for x in range(len(l) - 1):
    if l[x] > sr and l[x+1] > sr:
        if str(l[x] + l[x + 1])[-2:] == '31':
            ct += 1
            d.append(l[x] + l[x + 1])
print(ct, max(d))