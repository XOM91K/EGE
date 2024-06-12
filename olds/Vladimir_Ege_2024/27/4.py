l = [int(x) for x in open('4.txt')]
mx = 0
for i in range(len(l)):
    for j in range(len(l)):
        for g in range(len(l)):
            if i < j < g:
                if abs(i - j) == 123 or abs(j - g) == 123:
                    mx = max(mx, l[i] + l[j] + l[g])
print(mx)