ct=[]

for y in range(9,18):
    for x in range(0, y):
        c1 = 5 * 18 ** 3 + x * 18 ** 2 + y * 18 + 10
        c2 = 1 * y ** 3 + 8 * y ** 2 + x * y + 7
        ct.append(c1+c2)
print(len(set(ct)))