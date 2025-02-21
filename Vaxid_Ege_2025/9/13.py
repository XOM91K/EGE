l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    pov = []
    nepov = []
    for y in x:
        if x.count(y) == 3:
            pov.append(y)
        if x.count(y) == 1:
            nepov.append(y)
    if len(pov) == 3 and len(nepov) == 3:
            if sum(nepov) / len(nepov) < sum(pov):
                ct = ct + 1
print(ct)