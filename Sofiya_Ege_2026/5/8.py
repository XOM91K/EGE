def f7(n):
    s=''
    while n>0:
        s=str(n%7)+s
        n//=7
    return s
for n in range(1, 1001):
    r=f7(n)
    if n%2==0:
        r='52'+r+'1'
    else:
        r=r[-1]+r[1:-1]+r[0]+'15'
    r = str(int(r))
    if len(r)==4:
        print(n, r)
# R = '0000000001111111000000111111111111111'
# print(str(int(R))