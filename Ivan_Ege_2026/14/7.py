def ton(a, n):
    s = []
    while a > 0:
        s.append(a % n)
        a //= n
    return s[::-1]
a = 39 * 15**64 + 35**450 + 74 * 43**121 - 450035
for n in range(2, 100):
    b = ton(a, n)
    print(n, b.count(8))