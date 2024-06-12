ct = 0
l = [sorted([int(d) for d in x.split()]) for x in open('8.txt')]
for x in l:
    if len(set(x)) == 2 and 90 not in x and x.count(x[1]) != 3:
        ct += 1
print(ct)
#60 60 60 30