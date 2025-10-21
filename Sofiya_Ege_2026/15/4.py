def f(x):
    return (x&A==0)<=((x&31!=0)<=(x&35!=0))
ct = 0
for A in range(50, 121):
    if all(f(x)==1 for x in range(1, 10000)):
        print(A)