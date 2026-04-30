p = 5
q = 7
e = 11
for d in range(40):
    if (d * e) % ((p - 1) * (q - 1)) == 1:
        print(d)