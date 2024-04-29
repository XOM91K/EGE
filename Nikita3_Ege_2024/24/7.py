s = open('7.txt').readline()
s = s.split('A')
ct = 0
print(s)
for x in s:
    if len(x) <= 12 and 'B' not in x:
        ct += 1
print(ct)