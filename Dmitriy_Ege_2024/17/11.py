l = [int(x) for x in open('11.txt')]
mn_19 = 10 ** 10
ct = 0
mx = 0
for x in l:
    if x % 19 == 0 and x > 0:
        mn_19 = min(mn_19, x)
for x in range(len(l)- 1):
    if (l[x] + l[x + 1]) < mn_19:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])

print(ct, abs(mx))