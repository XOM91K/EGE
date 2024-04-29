mn=10**10
mn2=10**10
ct =0
l = [int(x) for x in open('7.txt')]
for x in l:
    if str(x)[-1] == '3' and len(str(abs(x))) == 3:
        mn = min(mn,x)
print(mn)
for x in range(len(l) - 1):
    if ((len(str(abs(l[x])))== 4 and len(str(abs(l[x+1]))) != 4) or (len(str(abs(l[x])))!= 4 and len(str(abs(l[x+1]))) == 4)) and ((l[x]**2 + l[x+1]**2)%mn ==0):
        ct+=1
        mn2 = min(mn2,(l[x]**2 + l[x+1]**2))
print(ct,mn2)