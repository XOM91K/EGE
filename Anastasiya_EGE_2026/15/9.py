n = 35000
for a in range(n, 1, -1):
    can=True
    for x in range(1, n):
        if ((x%332==0)<=((x%a!=0) <= (x%412!=0)))==0:
            can=False
    if can:
        print(a)
        break