mn = 10 ** 10
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        R = R + bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R > 151:
        if R < mn:
            mn = R
print(mn)

# s = 'СОЛНЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫШКО'
# print(s[1:5])
# print(s[-3:])