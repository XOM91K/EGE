l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    dl = [d for d in x if d % 3 == 0]
    ndl = [d for d in x if d % 3 != 0]
    if len(dl) == 3:
        if len(ndl) == 3:
            x.sort()
            if x[5] - x[0] <= sum(dl):
                ct += 1

print(ct)