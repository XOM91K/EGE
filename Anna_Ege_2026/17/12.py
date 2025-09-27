l = [int(x) for x in open('12.txt')]
ct = 0
s = []
mn = [y for y in l if abs(y) % 100 == 68]
for x in range(len(l)-1):
    k = 0
    if str(l[x])[-2:] == '68':
        k += 1
    if str(l[x+1])[-2:] == '68':
        k += 1
    if k == 1:
        if ((l[x] **  2) + (l[x+1] ** 2)) >= min(mn)**2:
            s.append(l[x]**2 + l[x+1]**2)
            ct += 1
print(ct, max(s))