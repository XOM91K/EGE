l=[int(x) for x in open('15.txt')]
ct=0
mx = 0
mn_ch = min([x for x in l if abs(x) % 100 == 25])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2:
        if l[x] * l[x+1] * l[x+2] <= mn_ch ** 2:
            ct += 1
            mx = max(mx, l[x] * l[x + 1] * l[x + 2])
print(ct)
print(mx)