l = [[int(d) for d in x.split()] for x in open('16.txt')]
ct = 0
for x in l :
    x = sorted(x)
    ar = ((x[0]+x[1]+x[2]+x[3]+x[4])/5)
    if x.count(x[-1]) == 1 :
        if len(set(x)) < 6 :
            if x[-1] > ar * 3:
                ct+=1
print(ct)