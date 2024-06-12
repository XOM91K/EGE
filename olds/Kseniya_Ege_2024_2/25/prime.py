d = 1231171111111
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return True
print(is_prime(d))
