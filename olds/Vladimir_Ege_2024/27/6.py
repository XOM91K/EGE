l = [int(x) for x in open('6.txt')]
mx = 0
K = 300
for i in range(len(l)):
    for j in range(len(l)):
        if i < j:
            if (l[i] + l[j]) % 101 == 0 and abs(i - j) >= K:
                mx = max(mx, l[i] + l[j])
print(mx)