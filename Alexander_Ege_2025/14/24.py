for x in range(21):
    c1 = 10*22**6+2*22**5+3*22**4+x*22**3+10*22**2+12*22
    c2 = 16*22**7+11*22**6+x*22**5+2*22**4+1*22**3+6*22**2+7*22
    if (c1+c2)%21==0:
        print((c1+c2) // 22)
