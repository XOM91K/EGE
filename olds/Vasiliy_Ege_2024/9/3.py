l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
k = 0
for x in l:
    k += 1
    if len(set(x)) != 6:
        povt = []
        for y in x:
            if x.count(y) > 1:
                povt.append(y)
        if sum(povt) / len(povt) < sum(x) / len(x):
            ct += k
print(ct)