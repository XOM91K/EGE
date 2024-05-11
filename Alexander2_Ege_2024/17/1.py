l = [int(x) for x in open('1.txt')]
mx35 = max([d for d in l if len(str(abs(d))) == 3 and str(d)[-1] == '5'])
ct = 0
mx = 0
for x in range(len(l) - 2):
    d = [str(l[x])[-1], str(l[x + 1])[-1], str(l[x + 2])[-1]]
    if d.count('5') == 1:
        if (l[x] + l[x + 1] + l[x + 2]) <= mx35:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)
