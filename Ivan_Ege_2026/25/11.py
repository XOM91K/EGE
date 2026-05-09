def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def deli(n):
    dels = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i) and '3' in str(i) and '5' in str(i):
                dels.append(i)
            if is_prime(n // i) and '3' in str(n // i) and '5' in str(n // i):
                dels.append(n // i)
    return sorted(set(dels))


for i in range(4_000_001, 10 ** 7):
    d = deli(i)
    if len(d) == 2 and (d[0] * d[1] * d[1] == i or d[1] * d[0] * d[0] == i):
        print(i, max(d))
