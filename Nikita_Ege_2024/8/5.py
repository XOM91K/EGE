import itertools
otv = 0
n = 0
for x in itertools.product('АПРСУ', repeat=5):
    n += 1
    for i in range(4):
        if x[i] != x[i+1] and x[i] != "A":
            otv =0
        else:
            break
    else:
        if x.count("У") <= 1:
            print(n, x)
            break