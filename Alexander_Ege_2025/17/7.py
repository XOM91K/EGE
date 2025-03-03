min_tr=[]
l = [int(x)for x in open("7.txt")]
k = [x for x in l if str(x)[-3:]=="151"]
sr = sum(k)/len(k)
for x in range(len(l)-2):
    s =[ n for n in [l[x],l[x+1],l[x+2]] if len(str(abs(n)))==4]
    if 0<len(s)<3:
        k13 = [ n for n in [l[x],l[x+1],l[x+2]] if n %13==0]
        k7 = [n for n in [l[x], l[x + 1], l[x + 2]] if n % 7 == 0]
        if len(k13)>len(k7):
            if l[x]>sr and l[x+1]>sr and l[x+2]>sr:
                min_tr.append(l[x]+l[x+1]+l[x+2])
print(len(min_tr),min(min_tr))