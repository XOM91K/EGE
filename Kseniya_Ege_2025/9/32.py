

l = [[int(d) for d in x.split()] for x in open('32.txt')]
k = 0

for x in l:
    k += 1
    if x == sorted(x):
        if (x[0] + x[-1]) / 2 < (x[1] + x[2] + x[3] + x[4] + x[5]) / 5:
            print(k, x)