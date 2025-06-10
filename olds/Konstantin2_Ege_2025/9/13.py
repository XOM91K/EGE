l = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
povt2 =[]
povt3 =[]
i = 0
for x in l:
    povt3= [v for v in x if x.count(v) == 3]
    povt2 = [z for z in x if x.count(z) == 2]
    if len(povt2) == 4  and len(povt3) == 3:
        k = 0
        if x[0] % 2 != 0:
            k += 1
        if x[1] % 2 != 0:
            k += 1
        if x[2] % 2 != 0:
            k += 1
        if x[3] % 2 != 0:
            k += 1
        if k == 2:
            i += sum(x)
print(i)