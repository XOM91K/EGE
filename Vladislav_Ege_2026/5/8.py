for n in range(1,10000):
    b=bin(n)[2:] # 1011000
    if b.count('0') > 0:
        b = b[:b.rindex('0')] + b[:2] + b[b.rindex('0') + 1:]
    else:
        continue
    b=b[::-1]
    b=int(b,2)
    if b==123:
        print(n)