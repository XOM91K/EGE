def v25(d):
    s = []
    while d > 0:
        s.append(d%25)
        d //= 25
    return s[::-1]
d = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 5*25**4 - 2025
print(v25(d))
print(v25(d).count(0))