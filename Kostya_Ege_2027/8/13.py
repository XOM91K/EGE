import itertools
k = 0
for x in itertools.product(sorted("ГОНДУБШ"), repeat=6):
    x = "".join(x)
    k += 1
    if k % 2 != 0:
        if "Б" not in x[0]:
            if x.count("Н") >= 2:
                if "У" not in x:
                    print(k,x)