l = [int(x) for x in open('17_5.txt')]
mx = 0
ct = 0
for x in l:
    if str(x)[-2:] == '15':
        mx = max(mx, x)
for x in range(len(l) - 2):
    if (len(str(l[x])) == 4 and len(str(l[x + 1])) != 4 and len(str(l[x + 2])) != 4) or (len(str(l[x])) != 4 and len(str(l[x + 1])) == 4 and len(str(l[x + 2])) != 4) or (len(str(l[x])) != 4 and len(str(l[x + 1])) != 4 and len(str(l[x + 2])) == 4):
        if (l[x] + l[x + 1] + l[x + 2]) >= mx:
            ct += 1
print(ct)