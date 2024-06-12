s = open('2.txt').readline()
s = s.replace('B', '@').replace('C', '@')
s = s.split('@')
print(s)