def tr(x, y, z):
    if x + y > z and y + z > x and z + x > y:
        return True
    return False

for A in range(1000):
    for x in range(1000):
        if (not((tr(x, 11, 18) == (not(max(x, 5) > 68))) and tr(x, A, 5))) == 0:
            break
    else:
        print(A)