def f(x, y):
    return (y<4) or (x>=20) or (3*x+y>A)
for A in range(0, 1000):
    if all(f(x, y)==1 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)