l = [int(x) for x in open('5.txt')]
l = l * 2
print(l)
mx = 0
for x in range(0, len(l) // 2):
    sm = 0
    for y in range(x, len(l) // 2 + x):
        sm += l[y]
        mx = max(mx, sm)
print(mx)
