l = [[int(d) for d in x.split()] for x in open('29.txt')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        if x[-1] > x[0] + x[1] + x[3]:
            povt = []
            nepovt = []
            for y in x:
                if x.count(y) == 2:
                    povt.append(y)
                if x.count(y) == 2:
                    nepovt.append(y)
            if len(povt) == 4:
                print(n, x)