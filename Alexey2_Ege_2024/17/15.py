l = [int(x) for x in open('15.txt')]
mx = 0
ct = 0
ms = 0

for x in l:
    if str(x)[-1] == '5' and len(str(abs(x))) == 3:
        mx = max(x,mx)
for x in range(len(l) - 2):
    if ((str(l[x])[-1] == '5' and str(l[x + 1])[-1] != '5' and str(l[x + 2])[-1] != '5')
            or (str(l[x])[-1] != '5' and str(l[x + 1])[-1] == '5' and str(l[x + 2])[-1] != '5')
            or (str(l[x])[-1] != '5' and str(l[x + 1])[-1] != '5' and str(l[x + 2])[-1] == '5')) \
            and ((l[x] + l[x + 1] + l[x + 2]) <= mx):
        ct += 1
        ms = max(l[x] + l[x + 1] + l[x + 2], ms)
print(ct, ms)