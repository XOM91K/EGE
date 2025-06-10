def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1


for n in range(0, 100):
    s = ">" + 39*'0' + n*'1' + 39*'2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace(">", "0")
    if is_prime(sum(map(int, s))):
        print(n)