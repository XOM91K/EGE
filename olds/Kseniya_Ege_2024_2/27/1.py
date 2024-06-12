l = [int(x) for x in open('1.txt')]
print(l)
mx = 0
for x in range(len(l)):
    for y in range(len(l)):
        for z in range(len(l)):
            if x != y and x != z and y != z:
                if abs(x - y) >= 155 and abs(y - z) >= 155 and abs(x - z) >= 155:
                    mx = max(mx, l[x] * l[y] * l[z])
print(mx)