import math

ct = 0
l = [[int(d) for d in x.split()] for x in open("11.txt")]
for x in l:
    povt = [d for d in x if x.count(d) == 2]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) == 4 and len(nepovt) == 2:

        if max(povt) ** 2 > math.prod(nepovt):
            ct += 1
print(ct)
