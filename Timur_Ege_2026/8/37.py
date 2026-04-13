def v75(d):
    s=[]
    while d>0:
        s.append(str(d%75))
        d//=75
    return s
for x in range(1,32001):
    c=75**314+75**118-x
    c=v75(c)
    if c.count('0') < 197:
        print(c.count('0'), x)