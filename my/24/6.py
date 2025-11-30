#ne resheno
import re
s = open(r'C:\Users\Zarif\Downloads\24_24977.txt').readline()
s = re.split(r'2.0.2.6', s)
mx = []
for x in range(len(s) - 10):
    ln = 0
    for y in range(11):
        ln += len(s[x + y])
    mx.append(ln + (7 * 10) + 12)
print(mx)
print(max(mx))