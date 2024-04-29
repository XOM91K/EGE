d = 8 ** 888 + 15 * 15 ** 1515 - 2 ** 444
d = oct(d)[2:]
ct = 0
for x in range(1, 7):
    ct += d.count('7' + str(x))
print(ct)