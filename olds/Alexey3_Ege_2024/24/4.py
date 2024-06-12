s = open('4.txt').readline()
s = s.replace('FAT', '#').replace('BAD', '#').split('#')
mn_ln = 10 ** 10
for x in range(len(s) - 1):
    mn_ln = min(mn_ln, len(s[x] + s[x + 1]) + 9)
print(mn_ln)