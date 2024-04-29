l = [int(x) for x in open('3.txt')]
ct = 0
k = 300
for i in range(len(l) - 1):
    for j in range(i + k, len(l)):
        if (l[i] + l[j]) % 25 == 0:
            ct += 1
print(ct)