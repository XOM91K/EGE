s = open('22.txt').readline()
s = s.replace('C', 'F')
s = s.replace('D', 'F')
s = s.replace('A', 'O')
s = s.replace('FFO', '#')
s = s.replace('FOO', '#')
s = s.replace('O', 'F')
s = s.split('F')
print(max(s, key=len))