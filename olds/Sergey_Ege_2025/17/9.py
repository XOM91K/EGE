l = [int(x) for x in open('9.txt')]
mx39 = 0
ct = 0
mx = 0
for x in l:
    if len(str(abs(x))) == 4 and str(x)[-2:] == '39':
        mx39 = max(mx39, x)
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4):
        if (l[x] + l[x + 1]) ** 2 <= mx39 ** 2:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)