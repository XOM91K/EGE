l=[int(x) for x in open(r'C:\Users\Zarif\Downloads\17 (47).txt')]
d=[]
ans=[]
for x in range(len(l)-1):
    n1=l[x]
    n2=l[x+1]
    if ((abs(n1)%9==0  and abs(n2) % 9 != 0 and int(oct(abs(n2))[2:])%10==3)+(abs(n2)%9==0 and abs(n1) % 9 != 0 and int(oct(abs(n1))[2:])%10==3))==1:
        ans.append(max(n1, n2))
print(len(ans), max(ans))