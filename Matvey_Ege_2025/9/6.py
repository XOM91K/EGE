l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if x[3] < x[0] + x[1] + x[2]:
        if x[0] + x[-1] == x[1] + x[2]:
            print(x)
            ct += 1
print(ct)