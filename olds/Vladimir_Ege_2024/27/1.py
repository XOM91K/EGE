l = [int(x) for x in open('1.txt')]
ct = 0
for i in range(len(l)):
    for j in range(len(l)):
        if i < j:
            if l[i] + l[j] >= 11023:
                ct += 1
print(ct)