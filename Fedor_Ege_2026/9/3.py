l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(povt1) == 3:
       if sum(povt1) / 3 < sum(povt3):
           ct += 1
print(ct)