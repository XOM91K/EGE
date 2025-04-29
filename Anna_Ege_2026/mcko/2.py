def F(p, q):
    return (p - 1) * (q - 1)
for d in range(0, 40):
    if (d * 11) % F(5, 7) == 1:
        print(d)