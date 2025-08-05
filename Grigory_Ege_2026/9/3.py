import math
l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) <= 6:
        nepovt = [y for y in x if x.count(y) == 1]
        povt = [y for y in x if x.count(y) >= 2]
        if 3 * sum(nepovt) <= math.prod(povt):
            ct += 1
print(ct)