l = [int(x) for x in open('1.txt')]
mx_19 = 0
ct = 0
mx = 0
for x in l:
    if x % 100 == 19:
        mx_19 = max(mx_19, x)
for x in range(len(l) - 2):
    k = 0
    if len(str(l[x])) == 4:
        k += 1
    if len(str(l[x + 1])) == 4:
        k += 1
    if len(str(l[x + 2])) == 4:
        k += 1
    if k == 2 and (l[x] % 3 == 0 or l[x + 1] % 3 == 0 or l[x + 2] % 3 == 0):
        if (l[x] + l[x + 1] + l[x + 2]) > mx_19:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)
