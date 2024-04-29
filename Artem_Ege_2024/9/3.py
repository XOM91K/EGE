l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
for x in l:
    # [15, 15, 17, 17, 39, 50, 45] set -> 5
    # [15, 15, 15, 1, 2, 3, 4] set -> 5
    if len(set(x)) == 5 and x.count(x[2]) != 3 and x.count(x[4]) != 3:
        if x[-1] != x[-2]:
            print(sum(x))