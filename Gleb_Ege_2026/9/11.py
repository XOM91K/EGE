l = [[int(d) for d in x.split()] for x in open('11.txt')]
ct = 0
k = 0
for x in l:
    k += 1
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4]:
        povt = [d for d in x if (sum(map(int, str(d))) % 2 == 0) and x.count(d) > 1]
        if len(povt) > 0:
            print(k)