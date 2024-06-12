# [5, 71, 13, 5, 71, 6]
# [2, 3, 4, 5, 5, 5, 9]
l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
for x in l:
    if len(set(x)) == len(x) - 2 and x.count(x[2]) != 3 and x.count(x[4]) != 3:
        print(x)