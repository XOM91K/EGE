k = 300
l = [int(x) for x in open('2.txt')]
ct = 0
for i in range(len(l)):
    for j in range(len(l)):
        if i < j:
            if abs(l[i] - l[j]) % 100 == 0 and ((l[i] % 37 == 0 and l[j] % 37 != 0) or (l[i] % 37 != 0 and l[j] % 37 == 0)):
                if abs(i - j) <= k:
                    ct += 1
print(ct)