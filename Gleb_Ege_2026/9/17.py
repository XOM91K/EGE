import itertools
l = [[int(d) for d in x.split()] for x in open('17.txt')]
for x in l:
    # 5 5 5 5 5 44 44
    # povt1 = [d for d in x if x.count(d) == 1]
    # if len(povt1) == 2:
    #     for y in itertools.combinations(x, 4):
    #         y = sorted(y)
    #         print(y)
    if len(set(x)) == 2:
        for y in itertools.combinations(x, 4):
            y = sorted(y)
            if y[0] == y[1] and y[2] == y[3]:
                if sum(y) < sum(x)-sum(y):
                    print(sum(x))
        # 22 22 88 88
# for x in itertools.combinations([5, 5, 5, 5, 5, 44, 44], 4):
#     print(x)