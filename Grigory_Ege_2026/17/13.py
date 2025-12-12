l = [int(d) for d in open('13.txt')]
m = max([y for y in l if len(str(abs(y))) == 5 and str(abs(y))[-1] == '3'])
msums = []
for x in range (len(l)-2):
    k = 0
    if len(str(abs(l[x])))== 5 and str(abs((l[x])))[-1:] == '3':
        k +=1
    if len(str(abs(l[x+1])))== 5 and str(abs((l[x+1])))[-1:] == '3':
        k +=1
    if len(str(abs(l[x+2])))== 5 and str(abs((l[x+2])))[-1:] == '3':
        k +=1
    if k >= 2 :
        if (l[x])**2+(l[x+1])**2+(l[x+2])**2 <= m ** 2 :
            msums.append((l[x])**2+(l[x+1])**2+(l[x+2])**2)
print(len(msums),min(msums))