l=[[int(d) for d in x.split()]for x in open('13.txt')]
ct=0
for x in l:
    povt3=[d for d in x if x.count(d)>=3]
    povt2=[d for d in x if x.count(d)==2]
    nepovt=[d for d in x if x.count(d)==1]
    if len(nepovt)>=1:
        if len(povt3) >= 3:
            if len(povt3)+len(povt2) != 0:
                if (sum(povt3)+sum(povt2))/(len(povt3)+len(povt2))>sum(nepovt)/len(nepovt):
                    ct+=1
print(ct)