l = [int(x) for x in open('7.txt')]
A = sorted(l[:1000])
B = sorted(l[1000:])
print(A[:5], A[-5:])
print(B[:5], B[-5:])
