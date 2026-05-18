l = [[int(d) for d in x.split()] for x in open('22.txt')]
ct = 0
for x in l:
    if x.count(max(x)) in [3, 4]:
        povt1 = [d for d in x if x.count(d) == 1]
        povt1 = sorted(povt1)
        if len(povt1) > 0 and povt1[0] + povt1[-1] <= sum(povt1[1:-1]):
            ct += 1
print(ct)