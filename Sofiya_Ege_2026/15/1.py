def f(x):
    return ((x%10==0) and(x%26==0) and (x>=300)) <= (A<=x)
for A in range(1000):
    if all(f(x)==1 for x in range(1000)):
        print(A)