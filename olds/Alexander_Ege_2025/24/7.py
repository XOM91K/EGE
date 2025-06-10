s = open(r'C:\Users\Zarif\Downloads\391_1 (3).txt').readline()
s = s.split('AXMM')
print(max(s, key=len))
print(len(max(s, key=len)) + 6)