l = [int(x) for x in open('3.txt')]
ct = 0
mx = 0
mx_39 = 0
for x in l:
    if abs(x) % 100 == 39 and len(str(abs(x))) == 4:
        mx_39 = max(mx_39, x)
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4):
        if (l[x] + l[x + 1]) ** 2 <= mx_39 ** 2:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)