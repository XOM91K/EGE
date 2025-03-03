l = [[int(d) for d in x.split()] for x in open('20.txt')]
k = 0
for x in l:
    k += 1
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4]:
    #if x == sorted(x):
        povt = [y for y in x if x.count(y) > 1 and sum(map(int, str(y))) % 2 == 0]
        if len(povt) > 0:
            print(k, x)