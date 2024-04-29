l = open('154_1.txt').readline().strip()
mx = 0
c=0
check="VWXYZ"*10**3

for i in range(len(l)):
    if l[i] in "VWXYZ" :
        g=check.find(l[i])
        h= check[g:]
        for j in range(0,100):
            if l[i]==h[j]:
                c+=1
                mx = max(mx, c)
            else:
                c=0
print(mx)