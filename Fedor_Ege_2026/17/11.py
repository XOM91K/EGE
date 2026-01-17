l = [int(x)for x in open('11.txt')]
mibpol = min([y for y in l if y > 0 and str(y)[-1:] == '6' and len(str(abs(y))) == 4])
xy =[]
for x in range(len(l)-2):
    k = 0
    if str(l[x])[-1] == '6' and len(str(abs(l[x]))) == 4:
        k += 1
    if str(l[x + 1])[-1] == '6' and len(str(abs(l[x+1]))) == 4:
        k += 1
    if str(l[x + 2])[-1] == '6' and len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k == 1:
        if l[x] + l[x+1] +l[x+2] <= mibpol:
            xy.append(l[x] + l[x+1] +l[x+2])
print(len(xy), max(xy))