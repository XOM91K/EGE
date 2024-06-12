l = [int(x) for x in open('12.txt')]
mn = 100**100
ct = 0
mn2 = 100**100
for x in l:
    if x %2 == 0:
        mn = min(x,mn)
print(mn)
for x in  range(len(l)-2):
    if (l[x]%2==0 and l[x+2]%2!=0) or (l[x]%2==0 and l[x + 2]%2!=0):
        if (l[x + 1] % mn == 0):
            mn2 = min(mn2,l[x]+l[x+2])
            ct+=1
print(mn2)
print(ct)
#1223 1225