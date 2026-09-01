a = int(input())
b = int(input())
for N in range(a, b + 1):
    # 3433
    for x in '0123456789':
        if str(N).count(x) == 3:
            print(N)