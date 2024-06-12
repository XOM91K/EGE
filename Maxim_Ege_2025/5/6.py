for N in range(1, 256):
    R = bin(N)[2:].zfill(8)
    #zfill - заливает нулями слева
    #replace - заменяет символы на новые символы
    ind1 = R.rindex('1')
    ch1 = R[:ind1]
    ch1 = ch1.replace('0', '#')
    ch1 = ch1.replace('1', '0')
    ch1 = ch1.replace('#', '1')
    ch2 = R[ind1 + 1:]
    ch2 = ch2.replace('0', '#')
    ch2 = ch2.replace('1', '0')
    ch2 = ch2.replace('#', '1')
    R = ch1 + '1' + ch2
    R = int(R, 2)
    print(N, R)
