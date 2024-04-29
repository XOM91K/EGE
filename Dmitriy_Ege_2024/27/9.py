M = 10
K = 122
ct = 0
l = [int(x) for x in open('9.txt')]
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if l[i] * l[j] * l[k] % M == 0 and abs(i - j) >= K and abs(j - k) >= K:
                ct += 1
print(ct)
