l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt1) == 4:
        if x.count(max(x)) == 1:
            ct += 1
print(ct)