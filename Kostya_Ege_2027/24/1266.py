# import re
# s = open(r'C:\Users\Zarif\Downloads\1266_1 (7).txt').readline()
# s = s.replace('AB','#')
# m = re.findall(r'(?=((?:[^#]*#){100}[^#]*))', s)
# print(max(m, key=len))
s = open(r'C:\Users\Zarif\Downloads\1266_1 (7).txt').readline()
s = s.split('AB')
ln = []
for x in range(len(s) - 100):
    lns = 0
    for y in range(0, 101):
        lns += len(s[x + y])
    ln.append(lns)
print(max(ln))
# s = 'dddddABdddddddddABddddddddd'
# print(len(s))
# s = 'dddABdddABdddddABdddddddddABdddddddddABdddABddd'
# s = s.split('AB')
# ln = []
# for x in range(len(s) - 2):
#     ln.append(len(s[x] + s[x + 1] + s[x + 2]))
# print(ln)
