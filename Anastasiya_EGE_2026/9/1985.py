l = [[int(d) for d in x.split()] for x in open('1985.txt')]
k = 0
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    povts = [y for y in x if x.count(y) > 1]
    if len(povt) >= 3 and len(nepovt) >= 1 and (sum(povts) / len(povts)) <= (sum(nepovt) / len(nepovt)):
        k += 1
print(k)
