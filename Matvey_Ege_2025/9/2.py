l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
ct = 0
for x in l:
    kr3 = []
    for i in x:
        if i % 3 == 0:
            kr3.append(i)
    if len(kr3) == 3:
        if x[-1] - x[0] <= sum(kr3):
            ct += 1
print(ct)