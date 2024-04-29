for i in range(100,1000):
     c = int(str(i)[0]) * int(str(i)[1])
     c1 = int(str(i)[1]) * int(str(i)[2])
     if str(min(c, c1)) + str(max(c,c1)) == "621":
          print(i)