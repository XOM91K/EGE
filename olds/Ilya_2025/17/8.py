a = [int(i) for i in open('8.txt')]
maxx=0
ct=0
minn = 10**10
for i in a:
    if len(str(abs(i)))==5 and abs(i)%100==25 and i>maxx:
        maxx=i
for i in range(len(a)-2):
    if (len(str(abs(a[i])))==5 and abs(a[i])%100==25) or (len(str(abs(a[i+1])))==5 and abs(a[i + 1])%100==25) or (len(str(abs(a[i+2])))==5 and abs(a[i + 2])%100==25):
        if (a[i]**2+a[i+1]**2+a[i+2]**2)<=maxx**2:
            ct+=1
            minn = min(minn, (a[i]**2+a[i+1]**2+a[i+2]**2))
print(ct, minn)