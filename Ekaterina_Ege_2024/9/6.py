l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    povt = []
    nepovt = []
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
        else:
            nepovt.append(y)
    if len(povt) > 0 and len(nepovt) > 0:
        if sum(nepovt) / len(nepovt) == sum(povt) / len(povt):
            ct += 1
print(ct)