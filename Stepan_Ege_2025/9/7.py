l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    if x[0] != min(x) and x[0] != max(x) and x[-1] != min(x) and x[-1] != max(x):
        x = sorted(x)
        if (x[-2] - x[1]) != 0:
            if (x[-1] - x[0]) % (x[-2] - x[1]) == 0:
                print(x)
                ct += 1
print(ct)