sm = 0
l = [sorted([int(d) for d in x.split()])for x in open("16.txt")]
for x in l:
    g = [i for i in x if x.count(i) == 3]
    f = [i for i in x if x.count(i) == 2]
    if len(g)==3 and len(f)==4:
        print(x, g, f)
        if (x[0]+x[1]) %2 == (x[2]+x[3]) %2 ==1 or (x[2]+x[1]) %2 == (x[0]+x[3]) %2 == 1 or (x[0]+x[2]) %2 == (x[1]+x[3]) %2 == 1:
            sm+=sum(x)
print(sm)