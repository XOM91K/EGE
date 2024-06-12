mn = 10 ** 10
#7302
for x in range(0, 1000):
    for y in range(0, 1000):
        if x + y >= 54:
            s = str(3 * x + 4 * y)
            if str(s)[::-1] == str(s):
                mn = min(mn, x * 2 + y)
print(mn)