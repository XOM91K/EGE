l = [int(x) for x in open('8.txt')]
K = 100
R = 50
ct = 0
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if abs(l[i] + l[j]) % 100 == 77 and R <= abs(i - j) <= K:
            ct += 1
print(ct)