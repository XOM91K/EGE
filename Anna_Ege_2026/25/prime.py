def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
#d = 137
d2 = 2147483647
#d3 = 121
print(is_prime(1))