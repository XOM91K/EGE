def prime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True
print(sum(x for x in range(1000) if prime(x)))