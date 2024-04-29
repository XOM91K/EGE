l = [int(x) for x in open('4.txt')]
k = 2
mx = 0
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if abs(i - j) >= k:
            mx = max(mx, sum(l[i:j + 1]))
print(mx)