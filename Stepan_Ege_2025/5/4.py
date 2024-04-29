for N in range(1, 256):
    R = bin(N)[2:].zfill(8)[:7][::-1]
    R = int(R, 2)
    if N == R:
        if R < 100:
            print(R)