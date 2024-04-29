ct = 0
for x in range(100,201):
    R = bin(x)[2:]
    if len(R) % 2 == 0:
        R = R + "10"
    else:
        R = "11" + R
    if int(R, 2) % 2 == 0:
        ct += 1
print(ct)