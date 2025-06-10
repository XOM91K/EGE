for N in range(0, 256):
    R = bin(N)[2:].zfill(8)
    R = R.replace("0", "£")
    R = R.replace("1", "0")
    R = R.replace("£", "1")
    R = int(R, 2)
    if R - N == 133:
        print(N)