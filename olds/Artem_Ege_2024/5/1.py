mn = 10**10
for x in range(100, 1000):
    c1 = int(str(x)[0]) + int(str(x)[1])
    c2 = int(str(x)[1]) + int(str(x)[2])
    if max(c1, c2) == 14 and min(c1, c2) == 12:
        mn = min(mn, x)
print(mn)