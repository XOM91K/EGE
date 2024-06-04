l = [sorted([int(d) for d in x.split()]) for x in open('21.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5 and (x.count(x[2]) == 3 or x.count(x[4]) == 3):
        if sum(x) < 502:
            print(x)
            ct += 1
print(ct)