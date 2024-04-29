l = [int(x) for x in open('3.txt')]
mn = min(l)
ct = 0
mx = 0
for x in range(len(l) - 1):
    if l[x] % 117 == mn or l[x + 1] % 117 == mn:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)