l = [int(x) for x in open('1.txt')]
sr = sum(l) / len(l)
ct = 0
mx = 0
for x in range(len(l) - 1):
    if (l[x] > sr or l[x + 1] > sr) and (l[x] % 17 == 0 or l[x + 1] % 17 == 0):
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)