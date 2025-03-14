l = [int(x) for x in open('4.txt')]
r = sorted(l)
med = r[len(r) // 2]
sr = sum(r) / len(r)
ct = 0
for x in range(len(r)):
    if sr <= r[x] <= med:
        ct += 1
print(ct)