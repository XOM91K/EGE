def v5(d):
    s=''
    while d>0:
        s = str(d % 5) + s
        d//=5
    return s
for x in range(1,4000):
    c=5**17-5**12-x
    c=v5(c)
    if c.count('0')>4:
        print(x, c.count('0'))