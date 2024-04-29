l = [int(d) for d in open('16.txt')]
print(l)
mx = 0
for i in range(len(l)):
    sm = 400_000
    j = i
    ct = 0
    while sm - l[j] >= 0 and j < len(l) - 1:
        sm -= l[j]
        ct += 1
        j += 1
    mx = max(mx, ct)
print(mx)