l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) == 3 and x.count(x[2]) != 3:
        print(x)