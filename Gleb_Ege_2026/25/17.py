def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
        return d>1
for x in range(700001, 10**10):
    if is_prime(x):