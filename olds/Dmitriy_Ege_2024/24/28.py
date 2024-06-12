
s = open(r'28.txt').readline()
s = s.replace('1', '@')
s = s.replace('3', '@')
s = s.replace('5', '@')
s = s.replace('7', '@')
s = s.replace('9', '@')
s = s.split('@@@')
mx = 0
print(max(s, key=len))