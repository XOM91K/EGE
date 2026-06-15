l = [[int(d) for d in x.split()] for x in open('1910.txt')]
for x in l:
    povt = [y for y in x if x.count(y) == 2]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 2 and len(nepovt) == 4:
        if (sum(nepovt) % povt[0]) == 0:
            print(sum(x))