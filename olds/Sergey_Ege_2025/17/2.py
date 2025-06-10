l = [int(x) for x in open('2.txt')]
mx_2 = 0
ct = 0
mx = 0
for x in l:
    if len(str(abs(x))) == 2:
        mx_2 = max(mx_2, x)
for x in range(len(l) - 1):
    if len(str(abs(l[x]))) == 2 or len(str(abs(l[x + 1]))) == 2:
        if (l[x] + l[x + 1]) <= mx_2:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)