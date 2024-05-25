s = open('3.txt').readline().split('Y')
mn_ln = 10 ** 10
for x in s:
    if x.count('X') >= 500:
        x = x.split('X')
        for y in range(len(x) - 498):
            ln = 0
            for z in range(499):
                ln += len(x[y + z])
            mn_ln = min(mn_ln, ln + 500)
print(mn_ln)