l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        elif x.count(y) == 1:
            nepovt.append(y)
    if len(povt) > 0 and (len(nepovt) == 0 or min(povt) > max(nepovt)):
        ct += 1
print(ct)