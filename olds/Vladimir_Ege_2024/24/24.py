s = open('24.txt').readline()
s = s.replace('X', '@')
s = s.replace('Y', '@')
s = s.replace('Z', '@')
s = s.split('@@')
print(s)
print(max(s, key=len))
#784