s = open('3.txt').readline()
s = s.replace('C', 'B')
s = s.replace('D', 'B')
s = s.replace('F', 'B')
s = s.replace('E', 'A')
s = s.split('A')
print(len(max(s,key=len)))