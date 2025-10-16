d = []
for x in range(0, 16):
    for y in range(0, 16):
        c1 = 2*16**5 + 7*16**4 + 10*16**3 + x*16**2 + 2*16**1 + 3*16**0
        c2 = 8*16**5 + y*16**4 + 14*16**3 + 5*16**2 + 13*16**1 + 2*16**0
        if (c1 + c2)%5 == 0:
            num = x + y
            #num2 = int(num, 16)
            d.append(num)
print(max(d))