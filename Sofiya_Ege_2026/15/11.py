def f(x, y):
    return (4*x+y>115) or (x>3*y) or (x+4*y<A)
for A in range(1, 10000):
    if any(f(x, y)==0 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)