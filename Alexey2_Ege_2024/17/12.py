l = [int(x) for x in open('12.txt')]
mx19 = 0
for x in l:
    if x % 19 == 0:
        mx19 = max(mx19, x)
ct = 0
mx = 0
for x in range(len(l) - 1):
    if l[x] > mx19 or l[x +1] > mx19:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)