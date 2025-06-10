import itertools
cnt = 0
ct = 0
g = 'ТИХО'
for word in itertools.product(sorted('ТИХОРЕЦК'), repeat=4):
    word = ''.join(word)
    worded = [d for d in word if d in 'ИОЕ']
    if len(worded) == 2 and (len(word) == len(set(word))):
        k = 0
        for x in range(4):
            if word[x] == g[x]:
                k += 1
        if k == 2:
            ct += 1
print(ct)