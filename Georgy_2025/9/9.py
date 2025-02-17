l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    if len(povt) == 3 and len(set(x)) == 4:
        if (sum(x) - sum(povt)) / 3 < sum(povt):
            print(x, povt)
            ct += 1
print(ct)