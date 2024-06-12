import itertools
l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        for y in itertools.permutations(x):
            if ((y[0] + y[1]) / 2) == ((y[2] + y[3]) / 2) == y[4]:
                ct += 1
                break
print(ct)