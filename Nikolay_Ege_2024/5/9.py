for n in range(11,10000):
    r=oct(n)[2:]
    if n%5==0:
        r = r + r[:3]
    else:
        r+=bin(n%5)[2:]
    if int(r, 8)>=35000:
        print(n)