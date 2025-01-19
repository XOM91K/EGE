d = 53**123 + 65**2222 - 172**12
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
sm = 0
for v in range(1, 6):
    sm += s.count('6' + str(v))
print(sm)