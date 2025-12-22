l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    x = sorted(x)
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        if x[-1] in nepovt:
            ct += 1
print(ct)