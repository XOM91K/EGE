import fnmatch
for x in range(12, 10**7 + 1, 12):
    k = 0
    mx_del = 0
    if fnmatch.fnmatch(str(x), '12*348'):
        for i in range(2, int((x ** 0.5) + 1)):
            if x % i == 0:
                k += 1
                if i != x // i:
                    k += 1
                    mx_del = max(mx_del, x // i)
    if k == 10:
        print(x, mx_del)