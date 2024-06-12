def v3(n):
    s=''
    while n > 0 :
        s+=str(n%3)
        n//=3
    return s[::-1]
for n in range(1,100):
    r=v3(n)
    if sum(map(int,r))%2==0:
        r='2'+r[2:]+'0'
    else:
        r = '20' + r[2:] + '1'
    if int(r,3)>75:
        print(n, int(r, 3))

# s='1234'
# print(s[2:]) -два левых разряда
