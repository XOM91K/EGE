for a in range(400, 1000):
   for x in range(1, 1000):
       for y in range(1, 1000):
           if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)) == 0:
               print(a)