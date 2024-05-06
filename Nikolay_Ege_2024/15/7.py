for A in range(500):
    Can=True
    for y in range(0, 500):
        for x in range(0, 500):
            if (((x>=A)or (121>=x**2))and((y**2<49)or(A<y)))==0:
                Can=False
                break
    if Can:
        print(A)