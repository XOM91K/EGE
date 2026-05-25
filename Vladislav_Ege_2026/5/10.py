for N in range(1,1000000):
    n=bin(N)[2:]
    if n.count("1")%4==0:
        n+="1111"
    elif n.count("1")%3==0:
        n="111"+n
    else:
        n+="11"
    n=int(n,2)
    if n<450 and n > 430:
        print(n)