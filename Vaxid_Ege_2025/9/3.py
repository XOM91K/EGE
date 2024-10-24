l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    if x[0] != min(x) and x[-1] != max(x) and x[0] != max(x) and x[-1] != min(x):
        x.sort()
        if (x[2] - x[1]) != 0:
            if (x[-1] - x[0]) % (x[2] - x[1]) == 0:
                ct += 1
print(ct)