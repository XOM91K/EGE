def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
ct = 0
for n in range(4, 1000):
    s = '3' + '5' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if prime(sum(map(int, s))) == True:
        print(n)
        ct += 1
print(ct)