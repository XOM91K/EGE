l = [sorted([int(d) for d in x.split()]) for x in open('9.txt')]
ct = 0
for x in l:
    kr3 = 0
    smkr3 = 0
    for y in x:
        if y % 3 == 0:
            kr3 += 1
            smkr3 += y
    if kr3 == 3:
        if (x[-1]- x[0]) <= smkr3:
            ct+=1
print(ct)