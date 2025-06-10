l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(nepovt) == 3 and len(povt3) == 3:
        if sum(nepovt) / len(nepovt) < sum(povt3):
            print(x)
            ct += 1
print(ct)