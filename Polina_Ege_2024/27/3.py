K = 324
l = [int(x) for x in open('3.txt')]
mx = 0
for i in range(len(l)):
    sm = 0
    for j in range(i, len(l)):
        sm += l[j]
        if j - i >= K:
            mx = max(mx, sm)
print(mx)