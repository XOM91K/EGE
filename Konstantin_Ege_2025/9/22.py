l = [[int(d) for d in x.split()] for x in open('22.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt) == 3:

    print(x)