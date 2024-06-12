def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for n in range(0,10000):
    r = v3(n)
    if n%2==0:
        r= '1'+ r+'00'
    else:
        r+=v3(sum(map(int,v3(n))))
    if int(r, 3)>168:
        print(n)