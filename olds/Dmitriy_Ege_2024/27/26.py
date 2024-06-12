l = [int(x) for x in open(r'26.txt')]
l += [0] * 21
mx = []
for x in range(len(l) - 21):
    for i in range(21, 200):
        if abs(l[x] - l[x + i]) % 2 != 0:
            if l[x] % 26 == 0 or l[x + i] % 26 == 0:
                mx.append(l[x] + l[x + i])
print(max(mx))