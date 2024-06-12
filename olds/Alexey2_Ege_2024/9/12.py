l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
k = 0
for x in l:
    k += 1
    if len(set(x)) == 5 and (x.count(x[1]) == 2 or x.count(x[2]) == 2 or x.count(x[3]) == 2 or x.count(x[4]) == 2 or x.count(x[5]) == 2 or x.count(x[6]) == 2 or x.count(x[7]) == 2) and (x.count(x[2]) == 3 or x.count(x[3]) == 3 or x.count(x[4]) == 3 or x.count(x[5]) == 3 or x.count(x[6]) == 3):
        print(k, x)