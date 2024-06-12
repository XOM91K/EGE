mn = 10 ** 10
def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
for x in range(100):#2
    for y in range(100):
        if x + y > 39:
            if prime(x * 3 + y * 4):
                mn = min(mn, x * 2 + y)
print(mn)