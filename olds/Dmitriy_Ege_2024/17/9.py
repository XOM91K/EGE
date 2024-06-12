l = [int(x) for x in open('9.txt')]
mx_3 = 0
mx = 0
ct = 0
for x in l:
    if len(str(abs(x))) == 5 and str(x)[-1] == '3':
        mx_3 = max(mx_3, x)
for x in range(len(l) - 2):
    if str(l[x])[-1] == '3' or str(l[x + 1])[-1] == '3' or str(l[x + 2])[-1] == '3':
        if (l[x] + l[x + 1] + l[x + 2]) <= mx_3:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)
