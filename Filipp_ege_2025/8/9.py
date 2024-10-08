from itertools import permutations
ct = 0
letters = 'ВЕБИНАР'
for p in permutations(letters, 7):
    flag = True
    for i in range(6):
        if (p[i] in 'ЕИА' and p[i + 1] in 'ЕИА') or (p[i] in 'ВБНР' and p[i + 1] in 'ВБНР'):
            flag = False
    if flag:
        ct += 1
print(ct)