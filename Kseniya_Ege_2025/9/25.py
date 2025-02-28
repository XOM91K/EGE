import math
l = [[int(d) for d in x.split()] for x in open('25.txt')]
ct = 0
for x in l:
    if len(set(x)) < 7:
        nepovt = [y for y in x if x.count(y) == 1]
        povt = [y for y in x if x.count(y) > 1]
        if sum(nepovt) * 3 <= math.prod(povt):
            ct += 1
print(ct)