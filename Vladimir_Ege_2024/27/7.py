l = [int(x) for x in open('7.txt')]
K = 7717
n = 17
ct = 0
for i in range(len(l)):
    for j in range(len(l)):
        for z in range(len(l)):
            if i < j < z:
                if abs(i - j) >= n and abs(j - z) >= n and abs(i - z) >= n:
                    if (l[i] + l[j] + l[z]) % K == 0:
                        ct += 1
print(ct)