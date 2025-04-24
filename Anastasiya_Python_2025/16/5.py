# MCKO
def f(p, q):
    return (p - 1) * (q - 1)
for d in range(0, 40):
    if d * 11 % f(5, 7) == 1:
        print(d)