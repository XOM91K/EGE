l = [int(x) for x in open('4.txt')]
mx = 0
ct = 0
mx_3 = 0
for x in l:
    if str(x)[-2:] == '25':
        mx = max(mx, x)
for x in range(len(l) - 2):
    if not(len(str(abs(l[x]))) == len(str(abs(l[x + 1]))) == len(str(abs(l[x + 2]))) == 4):
        if (l[x] + l[x + 1] + l[x + 2]) <= mx:
            ct += 1
            mx_3 = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx_3)
