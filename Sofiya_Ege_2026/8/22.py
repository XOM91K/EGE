import itertools
k=0
k2 = 0
for x in itertools.product(sorted('привычка'), repeat=5):
    x=''.join(x)
    k+=1
    if k % 5 != 0:
        k2 += 1
        if 'и' not in x and 'ы' not in x and 'а' not in x and len(set(x))==5:
            print(k2, x)