x = y = 0
x += 3
y += -3
for n in range (1,500):
    for a in range (-100,100):
        for b in range (-100,100):
            x += a
            y += b
            x += 27
            y += 15
        if x + 27 == 0 and y + 15 == 0:
            print(n)