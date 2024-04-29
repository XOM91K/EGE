def pt(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
sm = 0
for x in pt(d):
    sm += int(x)
print(sm)