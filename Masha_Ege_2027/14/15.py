s = 3 * 289**2024 + 81 * 49**121 - 9*16**81-6011
z = []
sm = 0
while s > 0:
    z.append(s%31)
    s = s//31
for x in range(18):
    sm += z.count(x) * x
print(sm)