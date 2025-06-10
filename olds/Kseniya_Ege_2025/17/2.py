l = [int(x) for x in open('2.txt')]
ct = 0
sr = sum(l) / len(l)
sm = []
for x in range(len(l) - 1):
    if l[x] > sr and l[x + 1] > sr:
        if str(l[x] + l[x + 1])[-2:] == '31':
            sm.append(l[x] + l[x + 1])
            ct += 1
print(len(sm), ct, max(sm))