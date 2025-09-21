l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(nepovt) == 3:
        if sum(nepovt) / len(nepovt) < sum(povt3):
            ct += 1
print(ct)