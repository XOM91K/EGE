l = [int(x) for x in open('3.txt')]
mx = []
for x in range(len(l) - 1):
    if abs(l[x] - l[x + 1]) % 2 == 0:
        if abs(l[x] - l[x + 1]) % 37 == 0:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))