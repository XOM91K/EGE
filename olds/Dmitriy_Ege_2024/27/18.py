l = [int(x) for x in open('18.txt')]
mx = 0
for x in range(len(l) - 1):
    sm = 0
    for y in range(x, len(l)):
        if y - 1 >= 0:
            sm += l[y] - l[y - 1]
            mx = max(mx, sm)
print(mx)