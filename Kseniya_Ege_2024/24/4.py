s = open('4.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D')
s = s.replace('F', 'D')
s = s.replace('DAA', '@')
s = s.replace('DDA', '@')
k = 1
while k * '@' in s:
    k += 1
print(k - 1)