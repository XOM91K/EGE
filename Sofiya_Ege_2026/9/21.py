l = [[int(d) for d in x.split()] for x in open('21.txt')]
k = 0
for x in l:
    k += 1
    x = sorted(x)
    povt1 = [a for a in x if x.count(a) == 1]
    if (len(povt1) == 0) + ((x[-1] + x[-2] + x[-3]) < (2 * (x[0] + x[1] + x[2]))) >= 1:
        print(k, x)
