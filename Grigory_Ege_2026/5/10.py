a = []
for N in  range(150,1000):
    R=bin(N)[2:]
    if R[-3:]=='101':
        R=R+'0'
    else:
        R += '11'
    R = int(R, 2)
    if R > 405:
        a.append(R)
print(min(a))
# R = '128931289'
# print(R[:-3:])
# print(R[-3:])