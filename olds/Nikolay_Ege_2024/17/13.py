l=[int(x)for x in open('8')]
ct=0
mx = 0
for x in range (len(l)-3):
    A=[]
    if (len(str(abs(l[x])))==2 and len(str(abs(l[x+1])))==2 and len(str(abs(l[x+2])))==2 and len(str(abs(l[x+3])))==2) or (len(str(abs(l[x])))==2 and len(str(abs(l[x+1])))!=2 and len(str(abs(l[x+2])))!=2 and len(str(abs(l[x+3])))!=2) or (len(str(abs(l[x])))!=2 and len(str(abs(l[x+1])))==2 and len(str(abs(l[x+2])))!=2 and len(str(abs(l[x+3])))!=2) or (len(str(abs(l[x])))!=2 and len(str(abs(l[x+1])))!=2 and len(str(abs(l[x+2])))==2 and len(str(abs(l[x+3])))!=2) or (len(str(abs(l[x])))!=2 and len(str(abs(l[x+1])))!=2 and len(str(abs(l[x+2])))!=2 and len(str(abs(l[x+3])))==2):
        if str(x)[-2:]=='68':
            A.append(x)
            if int(max(A)) < (l[x] + l[x + 1] + l[x + 2] + l[x+3]):
                ct+=1
                mx =max(mx, l[x] + l[x + 1] + l[x + 2]+l[x+3])
print(ct,mx)