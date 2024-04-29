ct = 0
l = [[int(d) for d in x.split()] for x in open('1.txt')]
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) == 2:#[20, 20, 40, 40, 56, 57]
            povt.append(y)
        elif x.count(y) == 1:
            nepovt.append(y)
    if len(povt) == 4 and len(nepovt) == 2:
        if x.count(max(x)) == 1:
            if (min(x) * max(x)) > (sum(x) - max(x) - min(x)):
                print(x, sum(x))
print(ct)