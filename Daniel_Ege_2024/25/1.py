def prime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
for x in range(6638225, 6638323):
    if prime(x):
        print(x)