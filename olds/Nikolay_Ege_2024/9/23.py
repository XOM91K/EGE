l=[sorted(int(d)for d in x.split())for x in open('23.txt')]
# print(l)
ct=0
for x in l:
    k=0
    if len(x)==len(set(x)):
        # print(x)
        k+=1
    if  (((x[0]+x[-1])*2)<=((x[1]+x[2]+x[3]+x[4]+x[5])*3)):
        k+=1
    if k==1:
        ct+=1
print(ct)