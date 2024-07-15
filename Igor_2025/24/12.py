import re

f = open('12.txt').readline().split('CD')
mx = 0
for x in range(len(f) - 50):
    ln = 0
    for y in range(51):
        ln += len(f[x + y])
    mx = max(mx, ln + 102)

#m = re.findall('\w*(?:CD\w*){50}', f)
print(mx)