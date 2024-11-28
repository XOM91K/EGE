l = [sorted([int(d) for d in x.split()]) for x in open('17.txt')]
ct = 0
for x in l:
    if (x[-1]+x[-2])*2 > (x[0]+x[1]+x[2])* 3:
        cifra5 = []
        for y in x:
            if str(y)[-1] == '5':
                cifra5.append(y)
        if len(cifra5) >= 2:
            ct += 1
print(ct)