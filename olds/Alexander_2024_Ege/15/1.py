# #kompege 7005
for A in range(1, 1000):
    for x in range(1, 1000):
        if ((((37 + A + x + 45) == 180) == ((A + x + 90) == 180)) and (A + 23 >= 120)) == 0:
            break
    else:
        print(A)
        