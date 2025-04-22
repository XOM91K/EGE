import itertools

alp = itertools.product(sorted('ПОБЕДА'), repeat=6)

i = 0
for s in alp:
    i += 1
    s = ''.join(s)
    if i%2==0:
        if s[0]=="О":
            if s.count('П') == 1 and s.count('О') == 1 and s.count('Б') == 1 and s.count('Е') == 1 and s.count('Д') == 1 and s.count('А') == 1:
                print(i, s)