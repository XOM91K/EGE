s = [x for x in open('2.txt')]
s = sorted(s)
s = [x.strip() for x in s]
print(', '.join(s))
