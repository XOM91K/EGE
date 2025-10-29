l = [int(x) for x in open('4.txt')]
m = sorted(l)[len(l) // 2]
sr = sum(l) // len(l)
ct = 0
for x in l:
    if sr <= x <= m:
        ct += 1
print(sr)
print(m)
print(ct)