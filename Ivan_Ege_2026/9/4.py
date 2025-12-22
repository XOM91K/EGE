l = [[int(d) for d in x.split()] for x in open('4.txt')]
c = 0
for x in l:
    x.sort()
    povt3 = [y for y in x if x.count(y) == 3]
    povt2 = [y for y in x if x.count(y) == 2]
    if len(povt3) == 3  and len(povt2) == 4:
        ct = 0
        for y in x[0:4]:
            if y % 2 == 0:
                ct += 1
        if ct == 2:
            c += sum(x)
print(c)