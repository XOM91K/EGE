for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0','$')
    R = R.replace('1','0')
    R = R.replace('$', '1')
    R = str(int(R))
    R = int(R,2)
    R = N - R
    if R == 1005:
        print(N)
# R = '0001010001010'
# R = R.replace('0','$')
# print(R)
# R = R.replace('1','0')
# print(R)
# R = R.replace('$','1')
# print(R)