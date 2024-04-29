l = [int(x) for x in open('11.txt')]
mx19 = 0
for x in l:
    if x % 19 == 0:
        mx19 = max(mx19, x)
ct = mx = 0
for i in range(len(l) - 1):
    if l[i] > mx19 or l[i + 1] > mx19:
        ct += 1
        mx = max(mx, l[i] + l[i + 1])
print(ct, mx)


