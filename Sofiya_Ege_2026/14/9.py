def f5(n):
    s=''
    while n>0:
        s=str(n%5)+s
        n//=5
    return s
d=0
for x in range(1, 2006):
    a=5**150+5**98-x
    ct=0
    b=f5(a)
    if b.count('0') > 55:
        print(x, b.count('0'))