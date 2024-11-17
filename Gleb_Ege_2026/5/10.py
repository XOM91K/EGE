for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0', '$')
    R = R.replace('1', '0')
    R = R.replace('$', '1')
    R = str(int(R))
    R = int(R, 2)
    R = N - R
    if R == 1005:
        print(N)

# s = '1111101011111000'
# s = s.replace('0', '$')
# s = s.replace('1', '0')
# s = s.replace('$', '1')
# print(s, str(int(s)))
# s = 'ОЛОВО'
# s = s.replace('О', 'А')
# print(s)