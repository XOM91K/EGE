l = [int(x) for x in open('11.txt')]
mx_25 = 0
ct = 0
mx = 0
for x in l:
    if str(x)[-2:] == '25':
        mx_25 = max(mx_25, x)
for x in range(len(l) - 2):
    if not(len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) == 4):
        if l[x] + l[x + 1] + l[x + 2] <= mx_25:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)