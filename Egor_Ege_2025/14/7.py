mx = -10**9
for p in range(1000, 9, -1):
    c = 39*15**64 + 35**450 + 74*43**121 - 450035
    s = []
    while c > 0:
        s.append(c % p)
        c //= p
    mx = max(mx, s.count(8))
    print(p, s.count(8))
print(mx)