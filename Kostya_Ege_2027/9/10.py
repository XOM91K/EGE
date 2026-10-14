import math
l = [[int(d) for d in x.split()] for x in open("10.txt")]
ct = 0
for x in l:
    povt = [d for d in x if x.count(d) >= 2]
    nepovt = [d for d in x if x.count(d) == 1]
    if sum(nepovt) * 3 <= math.prod(povt):
        if len(set(x)) < 7:
            ct += 1
            print(x, nepovt, povt)

print(ct)