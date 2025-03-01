ct=0
l = [sorted([int(d)for d in x.split()])for x in open("21.txt")]
for x in l:
    if x.count(x[-1])==1:
        povt = [i for i in x if x.count(i)>1]
        if len(povt) > 0:
            if (x[-1])/(sum(x[0:5])/5)>3:
                ct+=1
print(ct)