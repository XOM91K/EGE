s = open(r'C:\Users\Zarif\Downloads\1415_1 (4).txt').readline()
s = s.split('X')
mn = []
index = 0
for x in range(index, len(s) - 498):
    ln = 0
    for y in range(499):
        if 'Y' in s[x + y]:
            index = x + y
            ln += 10 ** 6
            break
        ln += len(s[x + y])
    mn.append(ln)
print(min(mn) + 500)
asdaYsdsYasadYsadasdas