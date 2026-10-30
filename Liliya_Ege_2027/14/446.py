def v15(d):
    s = []
    while d>0:
        s.append(str(d%15))
        d=d//15
    return s[::-1]
c=11*15**65+18*15**38-14*15**17+19*15**11+18338
c=v15(c)
print(len(set(c)))