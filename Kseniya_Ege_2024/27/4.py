l = [int(x) for x in open('4.txt')]
mx = 0
q = 81 * 3
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if abs(i - j) == q or abs(i - k) == q or abs(j - k) == q:
                mx = max(mx, l[i] + l[j] + l[k])
print(mx)
