l = [5, 1, 10, 3, 4]
ct = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] >= l[j]:
            ct += 1
            l[i], l[j] = l[j], l[i]
print(l, ct)