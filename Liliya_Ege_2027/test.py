l = [10, 20, 40, 45, 99, -5, 22]
l2 = []
for x in l:
    if x % 2 == 0:
        l2.append(x ** 2)
print(l2)
print([x ** 2 for x in l if x % 2 == 0])
