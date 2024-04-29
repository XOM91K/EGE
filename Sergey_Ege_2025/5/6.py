for N in range(1,1000):
     R = bin(N)[2:]
     if N % 3 ==0:
         R = R + R[-3:]
     else:
          a = (N % 3)*3
          R += bin(a)[2:]
     x = int(R, 2)
     if x >= 76:
          print(N)