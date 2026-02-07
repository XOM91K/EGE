import math
l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    if len(set(x)) < 7:
        povt = [d for d in x if x.count(d) >= 2]
        nepovt = [d for d in x if x.count(d) == 1]
        if sum(nepovt) * 3 <= math.prod(povt):
            ct += 1
print(ct)