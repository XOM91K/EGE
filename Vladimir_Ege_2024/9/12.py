l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
for x in l: # [22, 22, 22, 1, 2, 3, 4]
    povt = (sum(x) - sum(set(x))) // 2

    print(x)