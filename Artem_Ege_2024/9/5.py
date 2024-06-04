l=[sorted([int(d)for d in x.split()])for x in open('5.txt')]
k=0
for x in l:
    k+=1
    nepovt=[]
    povt2=[]
    povt3=[]
    for y in x:
        if x.count(y)==2:
            povt2.append(y)
        if x.count(y)==3:
            povt3.append(y)
        if x.count(y)==1:
            nepovt.append(y)
    if len(povt2)==2 and len(povt3)==3 and len(nepovt)==3 and povt3[0]>povt2[0]:
        print(k,x)
