def f(x):
    return (x % 12 == 0) and (70 <= x <= 80) and (x % A != 0)
ct = 0
for A in range(1, 10000):
    if all(f(x)==0 for x in range(10000)):
        ct += 1
print(ct)