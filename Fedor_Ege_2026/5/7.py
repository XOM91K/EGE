for N in range(10000, 100000):
    R = oct(N)[2:]
    R = R.replace('1', '2')
    R = R.replace('3', '2')
    R = R.replace('5', '2')
    R = R.replace('7', '2')
    R += str(N % 8)
    R = int(R, 8)
    d = R
    R = oct(d)[2:]
    R = R.replace('1', '2')
    R = R.replace('3', '2')
    R = R.replace('5', '2')
    R = R.replace('7', '2')
    R += str(d % 8)
    R = int(R, 8)
    if R % 2023 == 0:
        print(N)



# d = 123123
# print(bin(d)) # в 2-ую   #bin -> binary
# print(oct(d)) # в 8-ую   #oct -> octal
# print(hex(d)) # в 16-ую
