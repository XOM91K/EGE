l = [10, -5, 33, 122, -15, -58, 222, 12, 14, 1312, 123123, 456]
print([x for x in l if x % 3 == 0 and x > 0])
l2 = []
for x in l:
    if x % 3 == 0 and x > 0:
        l2.append(x)
print(l2)