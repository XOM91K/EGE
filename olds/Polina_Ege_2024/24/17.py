s = open('17.txt').readline()
#NPO, PNO
s = s.replace('NPO', '#').replace('PNO', '#')
s = s.replace('P', '$').replace('N', '$').replace('O', '$')
s = s.split('$')
print(len(max(s, key=len)))