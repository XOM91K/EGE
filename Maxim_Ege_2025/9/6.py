l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    x.sort()
    if (min(x) + max(x)) / 2 < (x[1] + x[2] + x[3] + x[4]) / 4:
        if len(set(x)) == 6:
            ct += 1
print(ct)
# [] list
# {} - ?
# () tuple
#