l = [int(x) for x in open('8.txt')]
mx_73 = 0
ct = 0
mx = 0
for x in l:
    if x % 73 == 0:
        mx_73 = max(mx_73, x)
for x in range(len(l) - 1):
    if l[x] >= mx_73 and l[x + 1] >= mx_73:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)