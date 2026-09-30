l=[]
for N in range(1,10000):
    R=bin(N)[2:]
    Nold = N
    for x in range(3):
        sm = sum(map(int, str(N)))
        if sm%2!=0:
            R=R+ '1'
        else:
            R=R+'0'
        N=int(R,2)
    if N>2064:
        l.append(N)
print(min(l))