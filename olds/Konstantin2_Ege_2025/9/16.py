l = [sorted([int(d) for d in x.split()]) for x in open('16.txt')]
ct = 0
for x in l:
    p =[v for v in x if v == max(x)]
    if len(p) == 1 and len(x) != len(set(x)):
        if max(x) > (x[0]+x[1]+x[2]+x[3]+x[4])/5 * 3:
            ct += 1
            print(ct)