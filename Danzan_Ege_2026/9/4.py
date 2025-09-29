l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[0]) == 1:
        if x.count(x[1]) >= 2 or  x.count(x[2]) >= 2 or x.count(x[3]) >= 2 or x.count(x[4]) >= 2 or x.count(x[5])>= 2:
            if (x[0] + x[5]) < 2*((x[1] + x[2] + x[3] + x[4])/4):
                ct += 1
                print(x)
print(ct)