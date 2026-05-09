l = [[int(d) for d in x.split()] for x in open('21.txt')]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    povtbol1 = [d for d in x if x.count(d) > 0]
    x = sorted(x)
    if (x[0] in povt3 and len(povt1) == 5) or (x[0] in povt2 and len(povt1) == 6):
        povt1 = sorted(povt1)
        if (povt1[0] ** 2 + povt1[-1] ** 2) <= sum(povt1[1:-1]) ** 2:
            ct += 1
print(ct)