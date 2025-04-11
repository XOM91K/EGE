l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    if x[0] != max(x) and x[0] != min(x) and x[-1] != max(x) and x[-1] != min(x):
        x.sort()
        if (x[-2] - x[1]) != 0:
            if (max(x) - min(x)) % (x[-2] - x[1]) == 0:
                ct += 1
print(ct)