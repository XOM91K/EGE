alf = '0123456789abcdef'
for N in range(1000):
    R = hex(N)[2:]
    sm_cif = 0
    for x in R:
        sm_cif += alf.index(x)
    if sm_cif %2 ==0:
        R+='f'
    else:
        R+='1'
    Res = int(R, 16)
    if Res <=300:
        print(N)