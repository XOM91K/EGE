def f(x,a):
    return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))

a = set([i for i in range(-1000,1000)])

for x in range(-1000, 1000):
    if not f(x,a):
        a.remove(x)
print(len(a) - 1)