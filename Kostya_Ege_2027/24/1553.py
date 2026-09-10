s = open('/Users/zarif/Downloads/1553_1.txt').readline()
s = s.replace('C', 'F').split('F')
print(len(max(s, key=len)))