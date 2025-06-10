import itertools
cnt = 0
for x in itertools.product(sorted('стары'), repeat=5):
    w = ''.join(x)
    cnt += 1
    if w[0] == 'с' and len(set(w)) == 5 and cnt % 2 != 0:
        print(cnt)