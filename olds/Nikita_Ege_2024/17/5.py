l = [int(x) for x in open('5.txt')]
otv = 0
mx = -10**9
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (((l[i] + l[j]) % 60 == 0) and ((l[i] % 40 == 0) or (l[j] % 40 == 0))):
            otv += 1
            mx = max(mx, l[i] + l[j])

print(otv,mx)