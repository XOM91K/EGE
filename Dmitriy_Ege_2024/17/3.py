l = [int(x) for x in open('3.txt')]
print(l)
sm_ch = 0
ct_ch = 0
ct = 0
mx = 0
for x in l:
    if x % 2 == 0:
        sm_ch += x
        ct_ch += 1
sr_ar = sm_ch / ct_ch
for x in range(len(l) - 1):
    if (l[x] % 3 == 0 and l[x + 1] < sr_ar) or (l[x] < sr_ar and l[x + 1] % 3 == 0):
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)