for x in range(0,10000):
    R = bin(x)[2:]
    if R.count("1") % 2 == 0:
        R = "1"+R+"00"
    else:
        R = "11"+R
    if int(R, 2) >= 412:
        print(x,int(R,2))