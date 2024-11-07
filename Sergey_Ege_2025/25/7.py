import fnmatch, time
ct = 0
start_time = time.time()
def dels(d):
    dls = []
    for x in range(1, d + 1):
        if d % x == 0:
            if x % 2 == 0:
                dls.append(x)
    return dls

for x in range(65001, 10**9):
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        g = dels(x)
        if len(g) >= 4:
            ct += 1
            print(x, sum(g))
    if ct == 8:
        break
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)