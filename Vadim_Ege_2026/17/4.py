l = [int(x) for x in open("4.txt")]
ms = []
m7 = min([x for x in l if abs(x)%10==7])
for x in range(0,len(l)-2):
   if len(str(abs(l[x]))) == 5 or len(str(abs(l[x+1]))) == 5 or len(str(abs(l[x+2]))) == 5:
       if (l[x]*l[x+1]*l[x+2]) % m7 == 0:
           ms.append(l[x]*l[x+1]*l[x+2])
print(len(ms), max(ms))
#print(-117 % 10)