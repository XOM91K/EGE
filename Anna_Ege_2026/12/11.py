mn = []
for c7 in range(12000):
    for c8 in range(12000):
        if len(str(c7 * 7 + c8 * 8)) == 6 and c7 >= 300:
            mn.append((c7 * 7 + c8 * 8) + (c7 + c8))
print(min(mn))