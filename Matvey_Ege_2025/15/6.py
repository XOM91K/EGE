for A in range(0, 10000):
    can = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            if (((4 * x + y) > 115) or (x > (3 * y)) or ((x + 4 * y) < A)) == 0:
                print(A)
                can = False
                break
        if can == False:
            break
# l = [1, 2, 10, 100, 5, -5]
# # l.sort()
# # print(l)
# # print(l.append(100))
# print(l.index(10))
# # print(sorted(l))