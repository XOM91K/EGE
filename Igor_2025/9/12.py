import math
l = [[int(d) for d in x.split()] for x in open('12.txt')]
for x in l:
    povt = [i for i in x if x.count(i) == 3]
    povtsqr = [i**2 for i in x if x.count(i) == 3]
    if len(povt) > 0:
        if sum(povtsqr) >= (sum(x) - sum(povt)) ** 2:
            print(sum(x))