l = [[int(d) for d in x.split()] for x in open('28.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) > 0 and len(nepovt) > 0:
        if x.count(max(x)) == 1:
            if sum(nepovt) / 3 >= sum(povt):
                ct += 1
print(ct)