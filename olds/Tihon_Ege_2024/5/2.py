for N in range(1, 256):
    R = bin(N - 1)[2:].zfill(8)
    R = R.replace('0', '$')
    R = R.replace('1', '0')
    R = R.replace('$', '1')
    R = int(R, 2)
    if R == 204:
        print(N)