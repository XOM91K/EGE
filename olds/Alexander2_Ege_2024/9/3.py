l = [[int(d) for d in x.split()] for x in open('3.txt')]
for x in l:
    if len(set(x)) == 5:
        if x.count(x[0]) != 3 and x.count(x[1]) != 3 and x.count(x[2]) != 3 and x.count(x[3]) != 3 and x.count(x[4]) != 3:
            if x.count(max(x)) == 1:
                print(x, sum(x))