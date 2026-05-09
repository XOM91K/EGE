import itertools
k = 0
for x in itertools.product(sorted("АРГУМЕНТ"), repeat=4):
    x="".join(x)
    k+=1
    if x[0] < x[1] < x[2] < x[3]:
        print(k, x)
print(int("4567", 8) + 1)