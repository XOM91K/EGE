def r(n):
    a = bin(n)[2::]
    if a.count('11') == 1:
        a += '0'
        b = '10' + a[2:]
    else:
        a += '1'
        b = '11' + a[2:]
    return int(b, 2)

mr = 0
mn = 0
for n in range(11, 10000):
    rr = r(n)
    if rr > mr and rr <= 1500:
        mr = rr
        mn = n
print(mn)