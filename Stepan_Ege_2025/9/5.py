l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
for x in l:
    if x[-1] != x[-2]:
        if len(set(x)) < 6:
            povt = []
            nepovt = []
            for y in x:
                if x.count(y) > 1:
                    povt.append(y)
                if x.count(y) == 1:
                    nepovt.append(y)
            if sum(povt) > sum(nepovt):
                ct += 1
print(ct)