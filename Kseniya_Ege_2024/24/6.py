s = open('6.txt').readline()
s = s.split('O')
d = [x for x in s if x.count('F') <= 2]
print(len(max(d, key=len)) + 2)