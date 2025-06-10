cnt = 0
k = 0
import itertools
for i in itertools.product(sorted("ПРИВЫЧКА"), repeat = 5):
    w = "".join(i)
    cnt += 1
    if cnt % 5 != 0:
        k += 1
        if len(set(w)) == 5 and 'И' not in w and 'Ы' not in w and 'А' not in w:
            print(k, w)