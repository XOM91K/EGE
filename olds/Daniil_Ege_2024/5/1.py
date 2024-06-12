for N in range(100, 1000):
    d = N
    ch1 = int(str(d)[0]) * int(str(d)[1])
    ch2 = int(str(d)[1]) * int(str(d)[2])
    if max(ch1, ch2) == 21 and min(ch1, ch2) == 6:
        print(N, ch1, ch2)
d = 'КАТУШКА'
print(d[3])
r = 987
r = str(r)
print(int(r[1]) + 2)
print(int(r[1]))
print(r[1])
print('8' + 2)
