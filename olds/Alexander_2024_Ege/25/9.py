l = []
def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
for n in range(10 ** 8 + 1, -1, -2):
    if prime(n):
        l.append(n)
    print(l)