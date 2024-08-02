l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    povt = []
    #[95, 26, 95, 26, 13, 13]
    # в строке три числа повторяются ровно по два раза;
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
    if len(povt) == 6:
        #– эти три числа образуют стороны прямоугольного треугольника
        if x[4] ** 2 == x[0] ** 2 + x[2] ** 2:
            ct += 1
print(ct)