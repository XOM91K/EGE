s = open(r'C:\Users\Zarif\Downloads\24_625_1 (1).txt').readline().replace('FAT', '#').replace('BAD','#')
#import re
#s = open(r'7.txt').readline().replace('FAT', '#').replace('BAD','#')
s = s.split('#')
mx = 10**10
for x in range(1, len(s) - 1):
    mx = min(mx, 9 + len(s[x]) + len(s[x + 1]))
print(mx)