n = 124800 # метод дихотомии
for A in range(n, 1, -1):
    can=True
    for x in range(1,n):
        if ((x%512==0)<=((x%A!=0)<=(x%243!=0)))==0:
            can=False
            break
    if can:
        print(A)
        break