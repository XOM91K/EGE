l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    kr3 = [y for y in x if y % 3 == 0]
    if len(kr3) == 3 and (x[-1] - x[0]) <= sum(kr3):
        ct += 1
print(ct)