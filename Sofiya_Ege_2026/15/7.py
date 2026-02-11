def f(x, y):
    return (x%A==0)<=(((x%55!=0)<=(y%101!=0)))
for A in range(1, 1000):
    if all(f(x,y)==1 for x in range(1, 1000) for y in range(1, 1000)):
        print(A)