l = [int(x) for x in open('6.txt')]
sr = sum(l) / len(l)
mn_sm = []
for x in range(len(l) - 1):
    if l[x] < sr or l[x + 1] < sr:
        if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x + 1] % 7 == 0 and l[x + 1] % 3 != 0 and l[x + 1] % 11 != 0 and l[x + 1] % 13 != 0):
            mn_sm.append(l[x] + l[x + 1])
print(len(mn_sm), min(mn_sm))
