l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
ct = 0
for x in l:
    if len(set(x)) != len(x):
        if x[-1] != x[-2]:
            povt = []
            nepovt = []
            for y in x:
                if x.count(y) > 1:
                    povt.append(y)
                else:
                    nepovt.append(y)
            if sum(povt) > sum(nepovt):
                ct += 1
print(ct)