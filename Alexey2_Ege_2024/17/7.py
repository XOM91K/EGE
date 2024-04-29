import fnmatch
l = [int(x) for x in open('7.txt')]
ct = 0
mx = 0
for x in range(len(l) - 2):
    pr = 1
    s = str(l[x]) + str(l[x + 1]) + str(l[x + 2])
    for y in s:
        pr *= int(y)
    if pr <= 2 * 10 ** 9 and fnmatch.fnmatch(str(pr), '55*2*'):
        ct +=1
        mx = max(mx, pr)
print(ct, mx)
