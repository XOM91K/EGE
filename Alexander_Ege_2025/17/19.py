l = [int(x) for x in open("19.txt")]
mn = min([i for i in l if len(str(abs(i)))==4 and i %17==0])
mx=[]
for x in range(len(l)-2):
    k=0
    if len(str(abs(l[x])))==4 and str(l[x])[-2:]=="27":
        k+=1
    if len(str(abs(l[x+1])))==4 and str(l[x+1])[-2:]=="27":
        k+=1
    if len(str(abs(l[x+2]))) == 4 and str(l[x+2])[-2:]=="27":
        k+=1
    if k>=1:
        if (l[x]**2+ l[x+1]**2 + l[x+2]**2)<=mn**2:
            mx.append(abs(l[x])+abs(l[x+1])+abs(l[x+2]))
print(len(mx),min(mx))