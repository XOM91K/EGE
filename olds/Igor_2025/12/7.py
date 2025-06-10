def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
mn_sm = 10 ** 10
for o in range(1, 100):
    for t in range(1, 100):
        if t + o >= 40:
            s = '0' + '1' * o + '2' * t
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1)
                s = s.replace('01', '220', 1)
            sm_cif = sum(map(int, s))
            if is_prime(sm_cif):
                mn_sm = min(mn_sm, o + t * 2)

print(mn_sm)