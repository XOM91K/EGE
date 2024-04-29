sm  =0
for N in range(10000, 100000):
   R = oct(N)[2:]
   for y in '13579':
       R = R.replace(y, '2')
   R += str(N%8)
   R = int(R,8)
   R = oct(R)[2:]
   for y in '13579':
       R = R.replace(y, '2')
   R += str(N%8)
   R = int(R,8)
   if R % 2023 == 0:
       sm += N
print(sm)