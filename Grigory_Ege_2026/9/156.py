l = [[int(d) for d in x.split()] for x in open('156.txt')]
ct = 0
for x in l :
    x = sorted(x)
    if x.count(x[0]) == 1 :
        if len(set(x)) <= 5 :
            povt = [y for y in x if x.count(y) >= 2]
            if x[-1]+x[0]< sum(povt):
                ct += 1
print(ct)