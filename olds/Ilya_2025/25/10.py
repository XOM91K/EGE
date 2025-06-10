def F(n):
    l=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            l.append(i)
            l.append(n//i)
    l = sorted(set(l))
    if len(l)<2 or l ==[]:
        return 0
    else:
        return max(l)-min(l)
ct=0
r = []
for i in range(1533878,0,-1):
    FF = F(i)
    if FF>5000 and FF%1235==0 and ct<=5:
        ct+=1
        r.append([i, FF])
        if ct == 5:
            break
for x in sorted(r):
    print(*x)