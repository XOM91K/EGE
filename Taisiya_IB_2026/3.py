n = '1,2,3,4,5; 4,5,6,7'
n = n.split(';')
n1 = n[0]
n2 = n[1]
print(n1,type(n1), "\n", n2, type(n2))
n1 = tuple(map(int,n1.split(',')))
n2 = set(map(int, n2.split(',')))
print(n1,type(n1), "\n", n2, type(n2))
intersection = set(n1).intersection(n2)
print(intersection)
diff = set(n1).difference(n2)
s = sorted(diff)
print(s)