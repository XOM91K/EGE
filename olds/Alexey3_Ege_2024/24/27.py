l = [int(x) for x in open('27.txt')]
mx = 0
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if l[i] > l[j] and l[k] > l[j]:
                mx = max(mx, (l[i] - l[j]) + (l[k] - l[j]))
print(mx)