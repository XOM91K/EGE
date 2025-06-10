l = []
for n in range(13, 1_000_000_000, 16):
    if n <= 789_012_345:
        l.append(n)
    else:
        break
print(l[-1], l[-2])