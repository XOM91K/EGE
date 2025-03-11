l = [[int(d) for d in x.split()] for x in open('11.txt')]
ct = 0
for x in l:
    if x.count(max(x)) == 1 and x.index(max(x)) < 4:
        if sum(x[:4]) / 4 < sum(x[4:]) / 4:
            ct += 1
print(ct)