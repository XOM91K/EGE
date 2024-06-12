s = open(r'31.txt').readline()
s = s.replace('AA', '@')
s = s.replace('AB', '@')
s = s.replace('AC', '@')
s = s.replace('BB', '@')
s = s.replace('BA', '@')
s = s.replace('BC', '@')
s = s.replace('CC', '@')
s = s.replace('CA', '@')
s = s.replace('CB', '@')
k = 0
while k * '@' in s:
    k += 1
print(k - 1)