import collections
s = open('34.txt').readline()
alf = collections.Counter(s)
s = s.replace('V', 'D')
s = s.replace('E', 'D')
s = s.replace('N', 'I')
s = s.replace('F', 'I')
#max: DVE
#min: INF
print(s.count('DI') + s.count('ID'))
#print(s)