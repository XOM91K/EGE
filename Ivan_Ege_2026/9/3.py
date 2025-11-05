l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    povt = [d for d in x if x.count(d) == 3]
    if len(set(x)) == 4 and len(povt) == 3:
        if (sum(x) - sum(povt)) / 3 < sum(povt):
            ct += 1
print(ct)