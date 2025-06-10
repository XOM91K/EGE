l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
for x in l:
    # [1, 1, 2, 2, 3]
    # [1, 1, 1, 2, 3]
    if len(set(x)) == 3 and x.count(x[2]) != 3:
        print(x)