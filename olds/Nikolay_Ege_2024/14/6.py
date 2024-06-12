for x in range(0,10000):
    d=8120 - 9**x + 50
    s=[]
    d = abs(d)
    while d>0:
        s.append(d%9)
        d//=9
    s=s[::-1]
    print(s)
    if sum(s)==138:
        print(x)