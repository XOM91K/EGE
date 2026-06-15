import itertools

k = 0
sm = []
for x in itertools.product(sorted('АВЕКЛМОРС'), repeat=7):
    k += 1
    x = ''.join(x)
    if 'А' not in x[:3] and 'В' not in x[:3] and 'Е' not in x[:3]:
        if x.count('Р') == 3:
            x = x.replace('А', '#')
            x = x.replace('В', '#')
            x = x.replace('Е', '#')
            x = x.replace('К', '#')
            x = x.replace('Л', '#')
            x = x.replace('М', '#')
            x = x.replace('О', '#')
            if x.count('С') == 1 and x.index('С') < x.index('Р') and 'РР' not in x:
                sm.append(k)
print(sum(sm))
