s = [int(x) for x in open('2.txt')]
k = 2
m = 10
l = 0
for i in range(len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for p in range(j + 1, len(s)):
            if j - i >= k and p - j >= k:
                if s[i] * s[j] * s[p] % m == 0:
                    l += 1
print(l)
