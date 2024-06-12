l = [int(x) for x in open('12.txt')]
mn_11 = 0
for x in l:
    if str(x)[-2:] == '25':
        mn_11 = max(mn_11, x)
print(mn_11)
ct = 0
mx = 0
for x in range(len(l) - 2):
    if not(len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) == 4):
        if (l[x] + l[x + 1] + l[x + 2]) <= mn_11:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)