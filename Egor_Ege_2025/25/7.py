def f(n):
    dels = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.append(i)
            dels.append(n // i)
        if len(dels) >= 2:
            return max(dels)
import fnmatch
for x in range(23, 10 ** 6 + 1, 23):
    m = f(x)
    if fnmatch.fnmatch(str(m), '6215'):

        print(x, m)