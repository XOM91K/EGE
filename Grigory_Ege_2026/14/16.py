def v5( d ):
    s=''
    while d != 0 :
        s += str(d%5)
        d//=5
    return s[::1]

for x in range (2005):
    d = 4 ** 163 * 5 + 12 ** 62 - x
    d = v5(d)
    if d.count('1')<d.count('4'):
        print(x)