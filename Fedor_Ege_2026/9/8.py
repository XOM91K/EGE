l = [[int(d) for d in x.split(',')] for x in open('8.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) >= 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) > 0:
        if len(povt1) > 0:
            povt = [y for y in x if x.count(y) >= 2]
            if sum(povt) / len(povt) < sum(povt1) / len(povt1):
                ct += 1
print(ct)