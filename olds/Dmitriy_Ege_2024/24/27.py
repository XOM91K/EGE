s = open(r'27.txt').readline()
s = s.replace('AHAHA', '@')
s = s.split('@')
print(len(max(s, key=len)) + 6)
#HAHAH