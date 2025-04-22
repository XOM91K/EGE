def v4(n):
    r=''
    while n!=0:
        r+=str(n%4)
        n//=4
    return r[::-1]


N = (4 ** 210) + (4 ** 110)

mx_cnt = 0
mx_n = 0
for x in range(1, 3_000+1):
    n = N - x
    n = v4(n)
    if n.count('0') > mx_cnt:
        mx_cnt = n.count('0')
        mx_n = x
print(mx_n)