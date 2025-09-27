def f(x):
    return ((x&103==0) and (x&94!=0))<=(x&A!=0)
for A in range(10000):
    if all(f(x)==1 for x in range(10000)):
        print(A)