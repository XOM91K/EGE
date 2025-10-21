def f9(n):
    s=''
    while n>0:
        s=str(n%9)+s
        n=n//9
    return s
for x in range(100):
    a=81**20-9**x+50
    b=f9(a)
    if sum(map(int, b)) == 138:
        print(x)