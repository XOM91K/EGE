c = 0
def dels(d):
    b = []
    for y in range(2, int(x ** 0.5)+1):
        if x%y == 0:
            b.append(y)
            b.append(x // y)
    return sorted(set(b))
for x in range(700000,10**7):
    b = dels(x)
    if len(b) >= 2:
        m = b[0] + b[-1]
        if m%10 == 4:
            print(x,m)
            c+=1
            if c == 5:
                break