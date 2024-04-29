import fnmatch
def max_del(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return n // x
for x in range(2023, 10 ** 8, 2024):
    if fnmatch.fnmatch(str(x), '13*7?5') and (1 + x) % 2024 == 0:
        print(x, max_del(x))