for N in range(1000):
    s=''
    zn=N
    while N > 0:
        s+=str(N%4)
        N//=4
    s = s[::-1]
    if sum(map(int, list(s)))%2==0:
        s='13'+s[2:]+'0'
    else:
        s='2'+s[:-2]+'13'
    if int(s,4)==167:
        print(zn)
        break