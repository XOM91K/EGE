import itertools
t = 0
for x in itertools.product(sorted('КОДИМ'), repeat=5):
    x = ''.join(x)
    t += 1
    if x.count('М') == 2 and 'ММ' not in x:
        print(t, x)