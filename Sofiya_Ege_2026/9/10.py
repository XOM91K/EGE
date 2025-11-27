f=open('10.txt')
k=0
for s in f:
    a=sorted([int(x) for x in s.split()])
    if len(set(a))==5:
        if (a[-1]+a[0]) / 2 == (a[-2]+a[1]) / 2 ==a[2]:
            k+=1
print(k)