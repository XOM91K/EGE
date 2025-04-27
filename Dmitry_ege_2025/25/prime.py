def is_prime(d):
    for x in range(2, d):
        if d % x == 0:
            return False
    return True

p = 121
print(is_prime(p))