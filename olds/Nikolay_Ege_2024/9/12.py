l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
for x in l:
    if x.count(x[2]) != 3 and x.count(x[3]) != 3 and len(set(x)) == 4:
        if x[-1] != x[-2]:
            if x[0] * x[-1] > x[1] + x[2] + x[3] + x[4]:
                print(x, sum(x))
                break