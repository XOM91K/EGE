v = []
for x in range(1, 25):
    a = 8*25**6 + 10*25**5 + 15*25**4 + 7*25**3 + x*25**2 + 1*25 + 1
    b = x*25**4 + 13*25**3 + 10*25**2 + 8*25 + 7
    for y in range(1, 101):
        if (a+b) % y == 0:
            v.append(y)
print(len(set(v)))