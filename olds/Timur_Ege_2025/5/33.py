for N in range(4,10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + R[:3]
    else:
        R = '1' + R + '01'
    R = int(R,2)  #в номере не написанно, что нужно переводить в 10
    if R > 600 and R < 620:
        print(R)