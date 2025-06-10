for N in range(1, 10000):
    R = bin(N)[2:]
    if R.rfind('0') == -1:
        continue
    R = R[:R.rfind('0')] + R[:2] + R[R.rfind('0') + 1:]
    R = R[::-1]
    R = int(R, 2)
    if R == 123:
        print(N)


#d = '124214412860174126'  ##
#print(d[:d.rfind('0')] + d[:2] + d[d.rfind('0') + 1:])