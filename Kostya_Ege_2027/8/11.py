import itertools
k = 0
k2 = 0
for x in itertools.product(sorted("ПРИВЫЧКА"), repeat=5):
    x = "".join(x)
    k += 1
    if k % 5 != 0:
        k2 += 1
        if len(set(x)) == 5:
            x = x.replace("Ы", "И")
            x = x.replace("А", "И")
            if "И" not in x:
                print(k2,x)