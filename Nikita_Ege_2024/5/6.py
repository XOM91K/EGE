otv = 0
for N in range(10_000, 100_000):
    r = N
    for j in range(2):
        r = oct(r)[2:]
        for i in '13579':
            r = r.replace(i, '2')
        r += str(N % 8)
        r = int(r, 8)
    if r % 2023 == 0:
        otv+= N
print(otv)