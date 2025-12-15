l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    if len(povt3) == 3 and len(set(x)) == 5:
        if x.count(max(x)) == 1:
            ct += 1
print(ct)