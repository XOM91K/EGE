def F(p, q):
    return (p - 1) * (q - 1)
for d in range(40):
    if (d * 11) % F(7, 5) == 1:
        print(d)
print(hex(32))