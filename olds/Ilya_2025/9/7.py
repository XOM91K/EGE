l = [sorted([int(d) for d in x.split()]) for x in open('7.txt')]
for x in l:
    if len(set(x)) == 2:
        print(x, sum(x))