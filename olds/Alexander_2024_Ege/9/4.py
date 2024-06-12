l = [[int(d) for d in x.split()] for x in open('4.txt')]
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
        if x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 4 and len(nepovt) == 3:
        if x.count(max(x)) == 1:
            print(sum(x))