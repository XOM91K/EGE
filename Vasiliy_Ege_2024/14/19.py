ct = 0
for x in range(0,18):
    y = (int('56'+str(x)+'3',18) + int('4'+str(x)+'9',18) - int('57'+str(x)+'1', 18))
    print(y)