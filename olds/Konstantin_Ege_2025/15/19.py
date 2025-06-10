for a in range(0, 500):
   can = True
   for x in range(0, 500):
       for y in range(0, 500):
           if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)) == 0:
               print(a)
               can = False
               break
       if can == False:
           break