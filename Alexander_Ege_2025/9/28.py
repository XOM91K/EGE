ct=0
l = [sorted([int(d) for d in x.split()]) for x in open("28.txt")]
for x in l:
    # 22 22 44 44 5 6 7
    povt = [i for i in x if x.count(i)==2]
    nepovt = [i for i in x if x.count(i)==1]

    if len(povt) == 4:
        if len(nepovt)==3:
            if x[0]*x[1]>x[2]+x[3]+x[4]+x[5]+x[6]:
                ct+=1
                print(x,povt,nepovt,ct)