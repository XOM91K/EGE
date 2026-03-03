def v4(d):
    s = ''
    while d>0:
        s += str(d%4)
        d//= 4
    return s[::-1] if d != 0 else '0'
d = []
for n in range(1, 1000):
    r = v4(n)
    if n % 2 == 0:
        r = '12' + r + v4(int(r[-1])*3)
    else:
        r = '13' + r + '21'
    r = int(r, 4)
    if n > 50:
        d.append(r)
print(min(d))