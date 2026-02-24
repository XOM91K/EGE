l = [[int(d) for d in x.split()] for x in open('15.txt')]
k = 0
for x in l:
    k += 1
    povt = [d for d in x if x.count(d) > 1]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) > 0 and len(nepovt) > 0:
        if sum(povt)**2 > sum(nepovt)**2:
            if sum(x) % 2 != 0:
                print(k)