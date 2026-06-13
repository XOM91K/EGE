def pros(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return n>1

def q(n):
    s = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    s = sorted(set(s))
    c = 0
    for e in s:
        c += e
    return c

for n in range(500001, 600000):
    w = q(n)
    a = int(w**0.5)
    if a**2 == w:
        if pros(a):
            print(n, w)