l = [int(x) for x in open('9.txt')]
mn_sm = 10 ** 10
k = 155
for i in range(len(l) - 2):
    for j in range(i + k, len(l) - 1):
        for r in range(j + k, len(l)):
            mn_sm = min(mn_sm, l[i] + l[j] + l[r])
print(mn_sm)