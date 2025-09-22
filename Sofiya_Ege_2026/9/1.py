l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    #в строке только одно число повторяется ровно два раза, остальные числа различны;
    if len(set(x)) == 4:
        x = sorted(x)
        if (x[-1] + x[0]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)