import math
l = [[int(d) for d in x.split()] for x in open('992.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) > 1]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) > 0:
        if sum(nepovt) * 3 <= math.prod(povt):

            ct += 1
print(ct)