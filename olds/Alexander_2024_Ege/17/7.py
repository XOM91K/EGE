l = [int(x) for x in open('7.txt')]
ct = mx = 0
mx_3 = max([x for x in l if str(x)[-1] == '3' and len(str(abs(x))) == 5])
for x in range(len(l) - 2):
    if str(l[x])[-1] == '3' or str(l[x + 1])[-1] == '3' or str(l[x + 2])[-1] == '3':
        if (l[x] + l[x + 1] + l[x + 2]) <= mx_3:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx )