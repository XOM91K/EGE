def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return n > 1
print(is_prime(1))
for n in range(1, 1000):
    s = '>' + '0' * 39 +'1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>' , 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '0')
    if is_prime(sum(map(int, s))) == True:
        print(n)
        break