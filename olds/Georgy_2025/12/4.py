def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


ct = 0
for n in range(10, 100):
    s = '1' + '0' * n
    while '10' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        if '1' in s:
            s = s.replace('1', '01', 1)
    if prime(len(s)) == True:
        ct += 1
        print(len(s))
print(ct)