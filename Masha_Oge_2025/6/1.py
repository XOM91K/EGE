for A in range(-100, 100):
    d = [(13, 2), (11, 12), (-12, 12),
         (2, -2), (-10, -10), (6, -5),
         (2, 8), (9, 10), (1, 13)]
    ctYes = 0
    for s, t in d:
        if s > A or t > 12:
            ctYes += 1
    if ctYes == 4:
        print(A)