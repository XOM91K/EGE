l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    x = sorted(x)
    povt = [d for d in x if x.count(d) > 1]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(set(povt)) == 2:
        if sum(set(povt)) < sum(povt1):
            ct += 1
print(ct)