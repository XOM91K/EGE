k = 155
l = [int(x) for x in open('2.txt')]
mx_sm = 10 ** 10
for x in range(len(l) - 2):
    for y in range(x + 1, len(l) - 1):
        for z in range(y + 1, len(l)):
            if abs(x - y) > k - 1 and abs(x - z) > k - 1 and abs(y - z) > k - 1:
                mx_sm = min(mx_sm, l[x] + l[y] + l[z])
print(mx_sm)