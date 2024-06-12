s=open("24_15339.txt").read()
c=0
mx=0
print(type(s))
for x in "ABC":
    s=s.replace(x,"+")
for x in "6789":
    s=s.replace(x,"-")
print(s)
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
    else:
        mx=max(mx,c)
        c=0
print(mx+1)




arr=sorted([int(x) for x in open("26_15341.txt")],reverse=True)
res=[arr[0]]
for i in range(1, len(arr)):
    if res[-1]-arr[i]>=8:
        res.append(arr[i])
print(len(res),res[-1])