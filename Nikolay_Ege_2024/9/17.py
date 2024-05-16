l = [[int(d) for d in x.split()] for x in open('17.txt')]
sm = 0
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 4 and len(nepovt) == 4:
        if x.count(min(x)) == 1:
            sm += sum(x)
            ct += 1
print(sm / ct)