def dels(x):
    b = []
    for y in range(2,int(x ** 0.5)+1):
        if x%y==0:
            b.append(y)
            b.append(x//y)
    b = sorted(set(b))
    return b[-2]+b[-1] if len(b) > 1 else 0
c = 0
for x in range(112_500_000,112_550_000):
    n = dels(x)
    if n != 0:
        if n%10000 == 1214:
            c+=1
            print(x)
            if c == 5:
                break