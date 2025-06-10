ct=0
l = [sorted([int(d)for d in x.split()])for x in open("30.txt")]
for x in l:
    ct+=1
    if x.count(x[-1])==3:
        nepovt = [i for i in x if x.count(i)==1]
        if len(nepovt)==4:
            print(ct,x, sum(x) / 7)