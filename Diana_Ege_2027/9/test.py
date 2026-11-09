l = [20, -20, -23, 24, 9, -1, 2, 100, 99]
l2 = []
for x in l:
    if x % 2 != 0:
        l2.append(x)
print(l2)
print([x for x in l if x % 2 != 0])