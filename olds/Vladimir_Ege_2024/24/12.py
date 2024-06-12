s = open('12.txt').readline()
s = s.replace('QW', '@')
s = s.split('@')
print(len(max(s, key=len)) + 1)