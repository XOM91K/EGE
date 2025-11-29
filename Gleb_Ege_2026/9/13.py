l = [[int(d) for d in x.split()] for x in open('13.txt')]
import math
ct = 0
for x in l:
    a = sorted([d for d in x if x.count(d) > 1])
    b = [d for d in x if x.count(d) == 1]
    pr = 1
    for d in a:
        pr *= d
    if len(set(x)) < 7 and sum(b) * 3 <= pr:
        print(x, a)
        ct += 1
print(ct)