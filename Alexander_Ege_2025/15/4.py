cnt = 0
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % 12 == 0) and (70 <= x <= 80) and (x % A != 0)) == 1:
            can = False
            break
    if can:
        cnt += 1
print(cnt)