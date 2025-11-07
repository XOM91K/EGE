s = open(r'C:\Users\Zarif\Downloads\391_1 (6).txt').readline()
s = s.replace('AXMM', '#')
s = s.split('#')
print(max(s, key=len))
# AXMM
print(len(max(s, key=len)) + 6)