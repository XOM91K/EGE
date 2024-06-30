l = [int(x) for x in open('9.txt')]
mx171 = 0
ct = 0
mn = 10 ** 10
for x in l:
    if x % 171 == 0:
        mx171 = max(mx171, x)
for x in range(len(l) - 1):
    if l[x] > mx171 or l[x + 1] > mx171:
        if '11' in str(l[x]) or '11' in str(l[x + 1]):
            ct += 1
            mn = min(mn, l[x] + l[x + 1])
print(ct, mn)