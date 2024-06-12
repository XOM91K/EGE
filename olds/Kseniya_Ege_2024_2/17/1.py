l = [int(x) for x in open('1.txt')]
mn = 10 ** 10
ct = 0
mx = 0
for x in l:
    if x % 17 == 0:
        mn = min(mn, x)
for x in range(len(l) - 1):
    if l[x] % mn == 0 or l[x + 1] % mn == 0:
        ct += 1
        mx = max(mx,l[x] + l[x + 1])
print(ct, mx)