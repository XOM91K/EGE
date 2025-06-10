K = int(input())
floor = cubes = 0
for i in range(K):
    floor += 1
    cubes += floor
    if cubes > K:
        print(floor - 1)
        break