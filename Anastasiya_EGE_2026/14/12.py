for x in range(37):
    for y in range(37):
        c=1*37**7 + 2*37**6 + x*37**5 + 6*37**4 + 4*37**3 + 3*37**2 + y*37 + 7
        if c%36==0:
            print(y * 37 + x)