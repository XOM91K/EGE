l =[sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if x[-1] ** 3 >= 2 * x[0] * x[1] * x[2]:
        if x[0] > 10 and x[1] > 10 and x[2] > 10 and x[3] > 10:
            ct += 1
print(ct)