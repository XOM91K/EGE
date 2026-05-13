def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def prost_mn(d):
    print(d)
    mn = []
    i = 2
    if is_prime(d) == False:
        while i < d:
            if is_prime(i) and d % i == 0:
                d //= i
                mn.append(i)
            else:
                i += 1
    return mn
for x in range(20262026 + 1, 10 ** 8):
    mndl = prost_mn(x)
    print(x, mndl)
