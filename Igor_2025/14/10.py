c = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 5*25**4 - 2025
s = []
while c > 0:
    s.append(c%25)
    c //= 25
s = s[::-1]
print(s)
print(s.count(0))