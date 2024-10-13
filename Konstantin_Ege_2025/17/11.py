l = [int(x) for x in open('11.txt')]
ct_pair = 0
mn_pair = 10 ** 10
sr = sum(l) / len(l)
for x in range(len(l) - 1):
    if l[x] < sr or l[x + 1] < sr:
        if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x + 1] % 7 == 0 and l[x + 1] % 3 != 0 and l[x + 1] % 11 != 0 and l[x + 1] % 13 != 0):
            ct_pair += 1
            mn_pair = min(mn_pair, l[x] + l[x + 1])
print(ct_pair, mn_pair)