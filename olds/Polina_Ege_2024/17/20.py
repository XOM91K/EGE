l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\17_9969 (1).txt')]
mx = 0
mx_ln = 0
ct = 0
mx2 = 0
for x in l:
    if len(set(str(abs(x)))) > mx_ln:
        mx_ln = len(set(str(abs(x))))
for x in l:
    if len(set(str(abs(x)))) == mx_ln:
        mx = max(mx, x)
for x in range(len(l) - 2):
    if (l[x] > 0 and int(l[x] ** 0.5) * int(l[x] ** 0.5) == l[x] and l[x + 1] + l[x + 2] >= mx) or \
            (l[x + 1] > 0 and int(l[x + 1] ** 0.5) * int(l[x + 1] ** 0.5) == l[x + 1] and l[x] + l[x + 2] >= mx) or \
            (l[x + 2] > 0 and int(l[x + 2] ** 0.5) * int(l[x + 2] ** 0.5) == l[x + 2] and l[x + 1] + l[x] >= mx):
        ct += 1


print(ct)