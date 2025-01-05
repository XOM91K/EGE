d = []
for N in range(16, 10000):
    R = bin(N)[2:]
    if R[1]=="1" and R[-2]=='0':
        R+=R[-2:]
    else:
        R="10"+R
    R=int(R,2)
    if R>151:
        d.append(R)
print(min(d))
# s = 'ПРИВЕТ'
# print(type(s[0]), type('П'))
# d = 1500[5:]
# print(5, type(0))