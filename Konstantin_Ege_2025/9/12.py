l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
ct = 0
for x in l:
    if x.count(x[2]) != 4:
        if x.count(x[2]) != 3 and x.count(x[3]) != 3:
            if len(set(x)) == 3:
                #эти три числа образуют стороны прямоугольного треугольника.
                if x[0] ** 2 + x[2] ** 2 == x[4] ** 2:
                    ct += 1
print(ct)