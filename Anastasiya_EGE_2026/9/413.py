l = [[int(d) for d in x.split()] for x in open('413.txt')]
ct = 0
for x in l:
    if x[0] != min(x) and x[0] != max(x):
        if x[3] != min(x) and x[3] != max(x):
            x = sorted(x)
            if (x[2] - x[1]) != 0:
                if (x[-1] - x[0]) % (x[2] - x[1]) == 0:
                    ct += 1
print(ct)
