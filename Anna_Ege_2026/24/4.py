s = open(r'C:\Users\Zarif\Downloads\391_1 (5).txt').readline()
print(len(max(s.split('AXMM'), key=len)) + 6)
print(max(s.split('AXMM'), key=len))