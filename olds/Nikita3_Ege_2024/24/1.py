s = open('1.txt').readline()
s = s.replace('C', 'F')
s = s.split('F')
print(len(max(s, key=len)))