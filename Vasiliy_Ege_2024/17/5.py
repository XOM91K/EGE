l = [int(x) for x in open('5.txt')]
mx_3 = 0
ct = 0
mx = 0
for x in l:
    if len(str(abs(x))) == 3 and str(sum(map(int, str(abs(x)))))[-1] == '3':
        mx_3 = max(mx_3, x)
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4):
        if (l[x] ** 2 + l[x + 1] ** 2) % mx_3 == 0:
            ct += 1
            mx = max(mx, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mx)