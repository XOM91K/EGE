import math
# 992
l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    povt = [d for d in x if x.count(d) > 1]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt) > 0:
        if sum(povt1) * 3 <= math.prod(povt):
            ct += 1
print(ct)