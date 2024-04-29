l=[[int(d)for d in x.split()]for x in open('8.txt')]
ct=0
for x in l:
    povt=[]
    x.sort()
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(povt) > 1 and x[0]!=x[1] and (x[0]+x[5])<sum(povt):
        ct += 1
print(ct)
