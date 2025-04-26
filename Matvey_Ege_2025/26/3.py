l = [int(x) for x in open('3.txt')]
# Метод с двумя указателями
l = sorted(l)
i = 0
j = len(l) - 1
ct = 0
while i <= j:
    if l[i] + l[j] == 100:
        ct += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > 100:
        j -= 1
    elif l[i] + l[j] < 100:
        i += 1
print(ct)