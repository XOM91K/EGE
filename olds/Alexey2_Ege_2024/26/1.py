l = sorted([int(x) for x in open('1.txt')])[::-1]
korjs = [max(l)]
for x in l:
    if korjs[-1] - x >= 8:
        korjs.append(x)
print(len(korjs), korjs[-1])