print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w <= (y == z)) and (y == (z <= x))) == 1 :
                    print(x, y, z, w)
#0:
# x y z w
# 0 0 0 1
# 1 0 0 0
#1:
# 0 0 1 0
# 0 1 0 0
# 1 1 0 0
# 1 1 1 0