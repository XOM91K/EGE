K = 123
l = [int(x) for x in open('15.txt')]
mx = -10 ** 7
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if abs(i - k) >= K and i != j and j != k and i != k:
                mx = max(mx, l[i] + l[j] + l[k])
print(mx)