l = [[int(d) for d in x.split()] for x in open('15.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if sum(x) < 0:
            ct += 1
print(ct)