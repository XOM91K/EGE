l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    povt2 = [y for y in x if x.count(y) == 2]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 2:
        print(x, povt3, povt2)
        if max(max(povt3), max(povt2)) > max(povt1):
            ct += 1
print(ct)