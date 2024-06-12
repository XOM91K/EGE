ct=0
for N in range(1,10000):

    R = bin(N)[2:]
    if N % 2 == 0:
        R = "1" + R + "11"
    else:
        R = "11" + R + '0'
    R =int(R,2)
    if R >=500 and R<=1000:
        ct+=1
        print(R,ct)