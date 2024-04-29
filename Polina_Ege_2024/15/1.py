m=0
for A in range (1,1000):
    k=0
    for x in range (1,1000):
        if ((160 <= x <= 180) <=((x%35 == 0) <= (x % A ==0))) == 1:
            k+=1
        if k== 999:
            m+=1
            print(m)