for x in range(0,95):
    for y in range(0,95):
        c1=1*95**4+x*95**3+y*95**2+x*95+5
        c2=6*95**4+y*95**3+x*95**2+1*95+7
        if (c1+c2)%4221==0:
            print(hex((c1 + c2) // 4221)[2:])

            print(x,y)
            print("-----")