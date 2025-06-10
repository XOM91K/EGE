l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if x[-1] < sum(x[:3]):
        if len(set(x)) == 3:
            ct += 1
print(ct)