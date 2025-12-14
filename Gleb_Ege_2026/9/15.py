l = [[int(d) for d in x.split()] for x in open('15.txt')]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) >= 3]
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(set(povt3)) >= 1 and len(set(povt1)) >= 1:
        if (sum(povt2) + sum(povt3)) / (len(povt2) + len(povt3)) > (sum(povt1) / len(povt1)):
            print(x, povt3, povt1)
            ct += 1
print(ct)
