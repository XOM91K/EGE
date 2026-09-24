import itertools
k = 0
slova = list(itertools.product('АИКЛМЬ', repeat=6))
slova = [''.join(x) for x in slova]
for x in slova:
    x = ''.join(x)
    k += 1
    if x[0] == 'К' and x[-1] == 'Ь' and len(set(x)) == 6:
        per = x[::-1]
        if per in slova:
            ind = slova.index(per)
            if abs(k - ind) == 26655 - 1:
                print(sum(map(int, str(k))), x,per)